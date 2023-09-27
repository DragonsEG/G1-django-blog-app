from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog, comment
from .forms import NewUserForm,BlogForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
            # If the Request was POST and the form data is valid, the form will be saved and the user will be created
            # save() returns the user object
			user = form.save()
            # This User will be logged in
			login(request, user)
            # Will be Redirected to Home page showing a success message
			messages.success(request, "Registration successful." )
			return redirect("showBlogs")
		messages.error(request, "Unsuccessful registration. Invalid information.")

	form = NewUserForm()
	return render (request, "Authentication/register.html", context={"form":form})

def loginView(request):
	if request.method == "POST":
        # Get Prepared Django Login Form and fill it with user's data coming from POST request
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
            # Validate username and password (user credentials)
			user = authenticate(username=username, password=password)
            # If the user is authenticated
			if user is not None:
                # This User will be logged in and will be 
				login(request, user)
                # Will be Redirected to Home page showing a success message
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("showBlogs")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "Authentication/login.html", context={"form":form})

def logoutRequest(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")

def createBlog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # Get the Form Data Sent by User
            form = BlogForm(request.POST or None)
            # Check that form has no common errors
            if form.is_valid():
                # Assign the form data to new post object to save it into DB
                blog = Blog(
                    author = request.user,
                    title= form.cleaned_data["title"],
                    content = form.cleaned_data["content"],
                )   
                # Save the post data into the DB
                blog.save()
                return redirect("showBlogs")
        else:
            # Get Django Post Form Created in forms.py
            form = BlogForm()
            
        context = {"form": form} 
        # Render home page with help of context data (the Dynamic content)          
        return render(request, "Blog/create.html", context)
    else:
        return redirect("login")
    
def showBlogs(request, search=None):
    if request.user.is_authenticated:
        # Get blogs Objects from Blog Model ordered by creation date and time in descending order
        blogs = Blog.objects.all().order_by("-created_at")
        context = {"Blogs": blogs} 
        # Render home page with help of context data (the Dynamic content)          
        return render(request, "Blog/home.html", context)  
    else:
        return redirect("login")

def blogPage(request, id):
    if request.user.is_authenticated:
        # Get object from Blog Model by its ID
        _blog = Blog.objects.get(ID=id)
        comments = comment.objects.filter(blog=_blog).order_by("-created_at")
        context = {"Blog": _blog , "Comments": comments} 
        # Render home page with help of context data (the Dynamic content)          
        return render(request, "Blog/blogPage.html", context)  
    else:
        return redirect("login")    
    
def addComment(request, blog_id):
    if request.user.is_authenticated:    
        if request.method == "POST":
            # Assign the form data to new post object to save it into DB
            _comment = comment(
                content = request.POST.get('comment'),
                user = request.user,
                blog = Blog.objects.get(ID=blog_id)
            )   
            # Save the post data into the DB
            _comment.save()
        return redirect("blogPage", id=blog_id)
    else:
        return redirect("login")      

def editBlog(request, blog_id):
    if request.user.is_authenticated:
        # Get object from Blog Model by its ID
        blog = Blog.objects.get(ID=blog_id)
        if request.method == "POST":
            # Get Django Blog Form Created in forms.py and apply old values (which exists in task) to its fields
            form = BlogForm(request.POST, instance=blog)
            # Check that form has no common errors
            if form.is_valid():
                # Update the object with the new values provided by the user. 
                # The `save()` method will automatically handle the update operation 
                # and persist the changes to the database. 
                form.save()
                return redirect("blogPage", id=blog_id)
        else:
            # Get Django Blog Form Created in forms.py and apply old values to its fields
            form = BlogForm(instance=blog)
            
        context = {"form": form}
        # Render home page with help of context data (the Dynamic content)        
        return render(request, "Blog/edit.html", context)  
    else:
        return redirect("login")

def deleteBlog(request, blog_id):
    if request.user.is_authenticated:
        obj = Blog.objects.get(ID=blog_id)
        obj.delete()
        return redirect("showBlogs")
    else:
        return redirect("login")    