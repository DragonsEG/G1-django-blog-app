from django.db import models
from django.contrib.auth.models import User , Group
# Create your models here.  
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_level = models.CharField(max_length=10, choices=[('viewer', 'Viewer'), ('writer', 'Writer'), ('admin', 'Admin')])
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=150) 
    
    def __str__(self):
      return self.name
class Tag(models.Model):
  category  = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='tags')
  tag_name  = models.CharField(max_length=100)
  
  def __str__(self):
    return self.tag_name
  
class Blog(models.Model):
  ID = models.BigAutoField(auto_created = True, primary_key=True, verbose_name="ID")
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_draft = models.BooleanField(default=True)
  publish_status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
  tags = models.ManyToManyField(Tag,related_name="tag_posts")
  
  def __str__(self):
      return self.title

class Comment(models.Model):
  ID = models.BigAutoField(auto_created = True, primary_key=True, verbose_name="ID")
  content = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)  
