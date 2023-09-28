from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Blog, comment
from .forms import NewUserForm,BlogForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q


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
            form = BlogForm(request.POST)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = request.user
                publish_status = form.cleaned_data.get('publish_status')
                is_draft = publish_status == 'draft'
                blog.is_draft = is_draft
                blog.save()
                
                return redirect("showBlogs")
        else:
            form = BlogForm()
        context = {"form": form}
        return render(request, "Blog/create.html", context)
    else:
        return redirect("login")

    
def showBlogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.all().order_by("-created_at")

    if query:
        blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {"Blogs": blogs, "query": query}
    return render(request, "Blog/home.html", context)

def blogPage(request, id):
        # Get object from Blog Model by its ID
        _blog = Blog.objects.get(ID=id)
        comments = comment.objects.filter(blog=_blog).order_by("-created_at")
        context = {"Blog": _blog , "Comments": comments} 
        # Render home page with help of context data (the Dynamic content)          
        return render(request, "Blog/blogPage.html", context)

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
    post = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            obj = Blog.objects.get(ID=blog_id)
            obj.delete()
            return redirect("showBlogs")
        else:
            return redirect("login")  
    return render(request, 'blog/post_delete.html', {'post': post})  
    
    
def publish_blog_post(request):
    query = request.GET.get('q')
    show_drafts = request.GET.get('show_drafts')  # Add this line

    # Filter based on the show_drafts parameter
    if show_drafts:
        posts = Blog.objects.filter(author=request.user, is_draft=True).order_by('-created_at')
    else:
        posts = Blog.objects.filter(author=request.user, is_draft=False).order_by('-created_at')

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    return render(request, 'blog/publish.html', {'posts': posts, 'show_drafts': show_drafts})  # Pass show_drafts to the template
