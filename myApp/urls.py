from django.urls import path
from . import views
from .views import category_list, category_post_list,category_list1
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
  path("", views.index, name="index"),
  path("register/", views.register, name="register"),
  path("login/", views.loginView, name="login"),
  path("logout", views.logoutRequest, name= "logout"),
  path("blog/create", views.createBlog, name="createBlog"),
  path("blog/", views.showBlogs, name="showBlogs"),
  path("blog/id/<int:id>/", views.blogPage, name="blogPage"),
  path("blog/AddComment/blog_id/<int:blog_id>/", views.addComment, name="addComment"),
  path("blog/edit/id/<int:blog_id>", views.editBlog, name="editBlog"),
  path("blog/delete/id/<int:blog_id>", views.deleteBlog, name="deleteBlog"),
  path('publish/', views.publish_blog_post, name='publish_blog_post'),
  path('not_allowed/', views.not_allowed, name='not_allowed'),
  path('blog/myBlog',views.myBlogPage,name='myblogpage'),
  path('blog/tagposts/<int:id>', views.tagposts, name='tagposts'),
  path("blog/joinRequests", views.joinRequest, name="joinRequest"),
  path("blog/approveReq/<int:company_id>/<int:request_id>", views.approveRequest, name="approveRequest"),
  path("blog/rejectReq/<int:request_id>", views.rejectRequest, name="rejectRequest"),
  path("blog/createCompany", views.createCompany, name="createCompany"),
  path("blog/myCompany", views.myCompany, name="myCompany"),
  path("blog/requestWriter", views.requestWriter, name="requestWriter"),
  path("blog/companyWriters", views.companyWriters, name="companyWriters"),
  path("blog/companyProfile/id/<int:company_id>", views.myCompany, name="companyProfile"),
  # ---------------------------------------------------------------------------
    path('blog/categories/', category_list, name='category_list'),
    path('blog/category/', category_list1, name='category_list1'),
    path('blog/categories/<int:category_id>/', category_post_list, name='category_post_list'),
    path('blog/create_category/', views.Category_create, name='category_create'),
    path('blog/edit_category/<int:category_id>/', views.category_edit, name='category_edit'),
    path('blog/delete_category/<int:category_id>/', views.category_delete, name='category_delete'),
    path('change-password/', PasswordChangeView.as_view(), name='password_change'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html',success_url='/password-change-done/'  ), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='blog/password_change_done.html'), name='password_change_done'),
    path('blog/userprofile/' , views.view_profile , name='user'),
    path('edit_user_name/', views.edit_user_name, name='edit_user_name'),
    path('leave_company/', views.leave_company, name='leave_company'),
]


    

