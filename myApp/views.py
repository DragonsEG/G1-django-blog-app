from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import Group,Permission  # Import the Group model at the top of your views.py
from django.contrib.auth.forms import PasswordChangeForm



def user_is_member(user):
    return user.is_superuser or not user.groups.filter(name='Viewer').exists()

def user_is_viewer(user):
    return user.is_superuser or user.groups.filter(name='Viewer').exists()

def isEmployee(user):
    return user.groups.filter(name='Employee').exists() or user.groups.filter(name='Manager').exists()

def isManager(user):
    return user.groups.filter(name='Manager').exists()

def index(request):
    return redirect("showBlogs")

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = request.POST.get('group')
            
            if group_name:  
                group, created = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)
                userProf = UserProfile(
                    user = user,
                    auth_level = group_name,
                    groups = group
                )
                userProf.save()
                # This User will be logged in
                login(request, user)
            # Will be Redirected to Home page showing a success message
            messages.success(request, "Registration successful.")
            return redirect("showBlogs")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request, "Authentication/register.html", context={"form": form})

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

def not_allowed(request):
    return render(request, 'Blog/not_allowed.html')

@user_passes_test(user_is_member, login_url='not_allowed')
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
                userProf = UserProfile.objects.get(user=request.user)
                blog.company = userProf.company or None
                blog.save()
                # Check if a category has been selected
                selected_categories = form.cleaned_data.get('categories')
                for selected_category in selected_categories:
                    blog.categories.add(selected_category)
                ## Tagging the post
                tags_input = form.cleaned_data.get('tags')
                if tags_input:
                    tags_list = [tag.strip() for tag in tags_input.split(',')]
                    categories = form.cleaned_data.get('categories')

                    existing_tags = Tag.objects.filter(tag_name__in=tags_list)
                    tag_instances = {}

                    for _tag_name in tags_list:
                        tag_instance = existing_tags.filter(tag_name=_tag_name).first()
                        if not tag_instance:
                            tag_instance = Tag.objects.create(tag_name=_tag_name)
                        tag_instances[_tag_name] = tag_instance
                    blog.tags.add(*tag_instances.values())

                    for category in categories:
                        for tag_instance in tag_instances.values():
                            tag_instance.category.add(category)

                return redirect("showBlogs")
        else:
            form = BlogForm()
        context = {"form": form}
        return render(request, "Blog/create.html", context)
    else:
        return redirect("login")

def showBlogs(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(publish_status="published").order_by("-created_at")
    categories = Category.objects.all()

    if query:
        blogs = blogs.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {"Blogs": blogs, "query": query,'categories': categories,}
    return render(request, "Blog/home.html", context)

def blogPage(request, id):
        # Get object from Blog Model by its ID
        _blog = Blog.objects.get(ID=id)
        comments = Comment.objects.filter(blog=_blog).order_by("-created_at")
        context = {"Blog": _blog , "Comments": comments} 
        # Render home page with help of context data (the Dynamic content)          
        return render(request, "Blog/blogPage.html", context)

def addComment(request, blog_id):
    if request.user.is_authenticated:    
        if request.method == "POST":
            # Assign the form data to new post object to save it into DB
            _comment = Comment(
                content = request.POST.get('comment'),
                user = request.user,
                blog = Blog.objects.get(ID=blog_id)
            )   
            # Save the post data into the DB
            _comment.save()
        return redirect("blogPage", id=blog_id)
    else:
        return redirect("login")      

@user_passes_test(user_is_member, login_url='not_allowed')
def editBlog(request, blog_id):
    if request.user.is_authenticated:
        # Get object from Blog Model by its ID
        blog = Blog.objects.get(ID=blog_id)
        if request.method == "POST":
            # Get Django Blog Form Created in forms.py and apply old values (which exists in task) to its fields
            form = EditBlogForm(request.POST, instance=blog)
            # Check that form has no common errors
            if form.is_valid():
                tags_input = form.cleaned_data.get('tags')
                
                if tags_input:
                    tags_list = [tag.strip() for tag in tags_input.split(',')]
                    categories = form.cleaned_data.get('categories')
                    
                    existing_tags = Tag.objects.filter(tag_name__in=tags_list)
                    tag_instances ={}
                    
                    for _tag_name in tags_list:
                        tag_instance = existing_tags.filter(tag_name=_tag_name).first()
                        if not tag_instance:
                            tag_instance = Tag.objects.create(tag_name=_tag_name)
                        tag_instances[_tag_name] = tag_instance
                        
                    form.instance.tags.clear()
                    form.instance.tags.add(*tag_instances.values())
                        
                    for category in categories:
                        for tag_instance in tag_instances.values():
                            tag_instance.category.add(category)

                    
                categories = form.cleaned_data.get('categories')
                form.instance.categories.set(categories)
                form.save()
                return redirect("blogPage", id=blog_id)
        else:
            # Get Django Blog Form Created in forms.py and apply old values to its fields
            initial_data = {'category': blog.categories.first()}  # Pre-select the current category
            form = EditBlogForm(instance=blog, initial=initial_data)
            
        context = {"form": form}
        # Render home page with help of context data (the Dynamic content)        
        return render(request, "Blog/edit.html", context)  
    else:
        return redirect("login")

@user_passes_test(user_is_member, login_url='not_allowed')
def deleteBlog(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            obj = Blog.objects.get(ID=blog_id)
            obj.delete()
            return redirect("showBlogs")
        else:
            return redirect("login")  
    return render(request, 'Blog/post_delete.html', {'post': post})  
    
def publish_blog_post(request):
    query = request.GET.get('q')  
    # Filter for only published blog posts
    posts = Blog.objects.filter(publish_status='published').order_by('-created_at')
    if query:
        posts = posts.filter(title__icontains=query)  # You can add more filters if needed
    return render(request, 'Blog/publish.html', {'posts': posts, 'query': query})

def myBlogPage(request):
    query = request.GET.get('q')
    author = request.user
    posts = Blog.objects.filter(author=author)
    if query: 
        posts = posts.filter(Q(title__icontains=query)|Q(content__icontains=query))
    return render (request, 'Blog/myblogpage.html', {'Blogs':posts,'query':query})

def tagposts(request,id):
    tag = Tag.objects.get(pk=id)
    posts = tag.tag_posts.all()
    query = request.GET.get('q')
    if query: 
        posts = posts.filter(Q(title__icontains=query)|Q(content__icontains=query))
    return render(request, 'Blog/tagposts.html', {'Blogs':posts,'tag':tag.tag_name, "query":query})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

@login_required
def category_list1(request):
    categories = Category.objects.all()
    return render(request, 'category/category.html', {'categories': categories})

@login_required
def Category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Your category was successfully created!')
            return redirect('category_list')
    else:
        form = CategoryForm()
        return render(request ,'category/category_create.html', {'form': form} )
        
        
@login_required
def category_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_edit.html', {'form': form, 'category': category})


@login_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully.')
        return redirect('category_list')
    return render(request, 'category/category_delete.html', {'category': category})


@login_required
def category_post_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Blog.objects.filter(categories=category, publish_status='published')
    return render(request, 'category/post_category.html', {'category': category, 'posts': posts})

@login_required
def joinRequest(request):
    requests = JoinRequest.objects.filter(user=request.user, status="Pending")
    emptyRequests = False
    if not requests:
        emptyRequests = True
    return render(request, 'blog/joinRequests.html', {'joinRequests': requests, "emptyRequests": emptyRequests})

@login_required
def approveRequest(request, company_id, request_id):
    userProf = UserProfile.objects.get(user=request.user)
    if userProf.company:
        messages.error(request,"Cannot Join a Company Because You're already in a one")
    else:    
        userProf.company = Company.objects.get(ID=company_id)
        userProf.save()
        # request.user.user_permissions.remove(permission)
        group = Group.objects.get(name='Employee')
        # Remove the user from existing groups
        request.user.groups.clear()
        # Add the user to the new group
        request.user.groups.add(group)
        
        joinRequest = JoinRequest.objects.get(id=request_id)
        joinRequest.status = 'Approved'
        joinRequest.save()
        
        messages.success(request, f"You are now member of {userProf.company.name} Company.")
        # ## Member who cannot add company is employee at the company
        # # Get the permission you want to remove
        # permission = Permission.objects.get(codename='add_company', content_type__model='company')
        # # Remove the permission from the user
    return redirect("joinRequest")

@login_required
def rejectRequest(request, request_id):
    joinRequest = JoinRequest.objects.get(id=request_id)
    joinRequest.status = 'Rejected'
    joinRequest.save()
    messages.info(request, "You have Rejected The Join Request.")
    return redirect("joinRequest")

@permission_required('myApp.add_company')
def createCompany(request):
    if request.user.is_authenticated:    
        if request.method == "POST":
            # Assign the form data to new post object to save it into DB
            _company = Company(
                name = request.POST.get('name'),
                manager = request.user,
            )   
            # Save the post data into the DB
            _company.save()
            # Get the group you want to assign
            group = Group.objects.get(name='Manager')
            # Remove the user from existing groups
            request.user.groups.clear()
            # Add the user to the new group
            request.user.groups.add(group)
            # Save the user
            request.user.save()
            userProf = UserProfile.objects.get(user=request.user)
            userProf.company = _company
            userProf.auth_level = "Manager"
            userProf.groups = group
            userProf.save()
            messages.success(request, f"You are the Manager of {_company.name} Company Now.")
            return redirect("myCompany")
        else:
            return render(request, "blog/createCompany.html")
    else:
        return redirect("login")
    
@user_passes_test(isEmployee, login_url='not_allowed')
def myCompany(request, company_id=None):
    if company_id:
        myCompany = Company.objects.get(ID=company_id)
    else:    
        userProf = UserProfile.objects.get(user=request.user)
        myCompany = userProf.company
        
    nEmployees = UserProfile.objects.filter(company=myCompany).count() - 1
    myCompanyBlogs = Blog.objects.filter(company=myCompany)
    
    query = request.GET.get('q')
    if query: 
        myCompanyBlogs = myCompanyBlogs.filter(Q(title__icontains=query)|Q(content__icontains=query))
            
    context = {"myCompany": myCompany, "companyBlogs": myCompanyBlogs, "nEmployees": nEmployees, "query": query} 
    return render(request, "blog/myCompany.html", context)

@user_passes_test(isManager, login_url='not_allowed')
def requestWriter(request):
    if request.method == "POST":
        form = RequestWriterForm(request.POST)
        if form.is_valid():
            userProf = UserProfile.objects.get(user=request.user)
            myCompany = userProf.company
            _user = form.cleaned_data["writer"]
            joinRequest = JoinRequest(
                user = _user,
                company = myCompany
            )
            joinRequest.save()
            messages.success(request, f"Your Request has been Sent to {_user.username} Successfully")
            return redirect("myCompany")
    else:
        form = RequestWriterForm()
    context = {"form": form}
    return render(request, "blog/requestWriter.html", context)


def companyWriters(request):
    thisWriter = UserProfile.objects.get(user=request.user)
    writers = UserProfile.objects.filter(company=thisWriter.company)
    context = {"writers": writers}
    return render(request, "blog/companyWriters.html", context)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'blog/change_password.html', {'form': form})


