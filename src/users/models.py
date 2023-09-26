from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from datetime import datetime
class UserManager(BaseUserManager):

    def create_user(self,username,email,password=None,*args,**kwargs):
        if username is None : raise TypeError("you must provide a username")
        if email is None : raise TypeError("you must provide a email address")
        if password is None : raise TypeError("you must provide a password")

        user =self.model(username=username,email=self.normalize_email(email),*args,**kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self,username,email,password=None,*args,**kwargs):
        if username is None: raise TypeError("you must provide a username")
        if email is None: raise TypeError("you must provide a email address")
        if password is None: raise TypeError("you must provide a password")

        user = self.create_user(username,email,password,*args,**kwargs)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser,PermissionsMixin):

    class UserGroups(models.TextChoices):
        Viewer = "VI", "Viewer"
        Writer = "WR", "Writer"
        Admin = "AD", "Admin"

    # public_id = models.UUIDField(unique=True.db_index=True,primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=60,unique=True,db_index=True)
    email = models.EmailField(unique=True,db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_group = models.CharField(max_length=2,db_index=True)
    is_superuser = models.BooleanField(default=False, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True,db_index=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
