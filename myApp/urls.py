from django.urls import path
from . import views

urlpatterns = [
  path("register/", views.register, name="register"),
  path("login/", views.loginView, name="login"),
  path("logout", views.logoutRequest, name= "logout"),
  path("blog/create", views.createBlog, name="createBlog"),
  path("", views.index, name="index"),
  path("blog/", views.showBlogs, name="showBlogs"),
  path("blog/id/<int:id>/", views.blogPage, name="blogPage"),
  path("blog/AddComment/blog_id/<int:blog_id>/", views.addComment, name="addComment"),
  path("blog/edit/id/<int:blog_id>", views.editBlog, name="editBlog"),
  path("blog/delete/id/<int:blog_id>", views.deleteBlog, name="deleteBlog"),
  path('publish/', views.publish_blog_post, name='publish_blog_post'),
  path('not_allowed/', views.not_allowed, name='not_allowed'),
  path('myblog/',views.myBlogPage,name='myblogpage'),
  path('tagposts/<int:id>', views.tagposts, name='tagposts'),
]