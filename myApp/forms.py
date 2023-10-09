from django import forms
from django.forms.widgets import DateTimeInput
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.db import models
from .models import Blog, Category, UserProfile, JoinRequest 
from .models import Company


class BlogForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={"placeholder": "Add the blog title"}),
    )
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Add your blog content"}))
    
    # Add the publish_status field
    PUBLISH_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    publish_status = forms.ChoiceField(
        label="Publish Status",
        choices=PUBLISH_CHOICES,
        widget=forms.RadioSelect(),
    )
    tags = forms.CharField(
        label="Tags",
        widget=forms.TextInput(attrs={"placeholder": "Add tags, separated by commas"}),
        required=False
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  
    )

    class Meta:
        model = Blog
        fields = [
            "title",
            "content",
            "publish_status",  # Include the publish_status field
            "tags",
            "categories"
        ]
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    

    # The constructor
    def __init__(self, *args, **kwargs):
        # Call the parent class __init__ method
        super().__init__(*args, **kwargs)  

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username", "password1", "password2"]
        
class EditBlogForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={"placeholder": "Add the blog title"}),
    )
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Add your blog content"}))
    
    # Add the publish_status field
    PUBLISH_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    publish_status = forms.ChoiceField(
        label="Publish Status",
        choices=PUBLISH_CHOICES,
        widget=forms.RadioSelect(),
    )
    tags = forms.CharField(widget=forms.TextInput(), required=False)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
        
        
    class Meta:
        model = Blog
        fields = ["title", "content","publish_status"]
        
        
    def __init__(self, *args, **kwargs):
    # Retrieve the 'blog' instance from the 'kwargs' if it was passed
        blog = kwargs.pop('instance', None)

        # Call the parent class __init__ method with 'instance' set to 'blog'
        super().__init__(instance=blog, *args, **kwargs)

        # Set the initial value for the 'tags' field as a comma-separated string of tag names
        if blog:
            self.fields['tags'].initial = ', '.join(tag.tag_name for tag in blog.tags.all())
            
            
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class RequestWriterForm(forms.ModelForm):
    writer = forms.ModelChoiceField(queryset=User.objects.all(), required=True)        
    
    class Meta: 
        model = JoinRequest
        fields = ['writer']
        
    # The constructor
    def __init__(self, *args, **kwargs):
        super(RequestWriterForm, self).__init__(*args, **kwargs)
        # Filter users by the "Member" group
        self.fields['writer'].queryset = User.objects.filter(groups__name='Member')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user' , 'company' , 'auth_level',]
        
        
        
class UserNameEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile  
        fields = ['photo']
        
        

class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Company name'
        self.fields['location'].widget.attrs['placeholder'] = 'Company location'
        self.fields['description'].widget.attrs['placeholder'] = 'Company description'