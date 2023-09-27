from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone





class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DRF', 'Draft'
        PUBLISHED = 'PUB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices = Status.choices, default = Status.DRAFT)

    class Meta:
        ordering = ["-publish"]

        indexes = [
            models.Index(fields=["-publish"]),
            
        ]


def __str__(self):
    return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ["created"]

        indexes = [
            models.Index(fields=["created"]),
        ]


def __str__(self):
    return f"Comment by {self.name} on {self.post}"
