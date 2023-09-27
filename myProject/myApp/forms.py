from django import forms
from django.forms.widgets import DateTimeInput
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(
      label="Title",
      widget=forms.TextInput(attrs={"placeholder": "Add the blog title"}),
    )
    content = forms.Textarea(attrs={"placeholder": "Add your blog content"})

    class Meta:
      # Specify the Model that the form represents
      model = Blog
      # the model fields to show
      fields = [
        "title",
        "content",
      ]
      
    # The constructor
    def __init__(self, *args, **kwargs):
        # Call the parent class __init__ method
        super().__init__(*args, **kwargs)  

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2")
  # super(NewUserForm, self).save(commit=False) line calls the save method of the parent class (UserCreationForm).
  # This parent class is responsible for handling the form data 
  # And creating a new instance of the User model with the provided data.
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user