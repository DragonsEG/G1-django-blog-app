from django import forms
from django.forms.widgets import DateTimeInput
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from .models import Blog
from django.db import models
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={"placeholder": "Add the blog title"}),
    )
    content = forms.Textarea(attrs={"placeholder": "Add your blog content"})
    
    # Add the publish_status field
    PUBLISH_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    publish_status = forms.ChoiceField(
        label="Publish Status",
        choices=PUBLISH_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = Blog
        fields = [
            "title",
            "content",
            "publish_status",  # Include the publish_status field
        ]
      
    # The constructor
    def __init__(self, *args, **kwargs):
        # Call the parent class __init__ method
        super().__init__(*args, **kwargs)  

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username", "password1", "password2"]
    # super(NewUserForm, self).save(commit=False) line calls the save method of the parent class (UserCreationForm).
    # This parent class is responsible for handling the form data
    # And creating a new instance of the User model with the provided data.
    # def save(self):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.save()
    #     # Add The User to Group User Called Writer (Has the Writer Permission)

    #     return user