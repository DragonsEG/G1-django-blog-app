from django.db import models
from django.contrib.auth.models import User , Group
from django.urls import reverse
# Create your models here.  
class Company(models.Model):
  ID = models.BigAutoField(auto_created = True, primary_key=True, verbose_name="ID")
  name = models.CharField(max_length=30)
  manager = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  location = models.CharField(max_length=100, null=True, blank=True)  
  description = models.TextField(null=True, blank=True)  


  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse("companyProfile", args=[self.ID,])
class Content(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
  
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="userprofile")
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
  auth_level = models.CharField(max_length=10, null=True, choices=[('viewer', 'Viewer'), ('member', 'Member'), ('admin', 'Admin'), ('manager', 'Manager')], default="Member")
  groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
  photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
  # user_name = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='profile')

  # def __str__(self):
        # return self.user.username
  def get_absolute_url(self):
    return reverse('userProfile',
                   args=[self.pk])

class JoinRequest(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
  company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
  status = models.CharField(max_length=10, choices=[('Pending', 'pending'), ('Approved', 'approved'), ('Rejected', 'rejected')], default="Pending")
  fromTo = models.CharField(max_length=20, choices=[("WriterToCompany", "WtoC"), ("CompanyToWriter", "CtoW")], default="CtoW")
  
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
  category  = models.ManyToManyField(Category,related_name='tags')
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
  categories = models.ManyToManyField(Category)
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
  
  def __str__(self):
      return self.title

  def get_absolute_url(self):
    
    return reverse("blogPage",args=[self.ID,])
class Comment(models.Model):
  ID = models.BigAutoField(auto_created = True, primary_key=True, verbose_name="ID")
  content = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=False)
  upVote = models.ManyToManyField(User, blank=True, related_name="upVotes")
  downVote = models.ManyToManyField(User, blank=True, related_name="downVotes")
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)