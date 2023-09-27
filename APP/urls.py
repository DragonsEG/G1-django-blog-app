from django.urls import path
from django.contrib import admin
from .views import ModelListView, BlogDetail ,CreateBlog ,UpdateViewBlog ,DeleteViewBlog ,CommentListView


urlpatterns = [
    path('',ModelListView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetail.as_view(), name='post_detail'),
    path('post/new/',CreateBlog.as_view(), name='post_new'),
    path('post/<int:pk>/edit',UpdateViewBlog.as_view(), name='post_edit'),
    path('post/<int:pk>/delete',DeleteViewBlog.as_view(), name='post_delete'),
    path('addcomment/', CommentListView.as_view(), name='add_comment'),

]



admin.site.index_title = 'Ahmed Tarek Radwan(ATR) 🦅 & Dragons 🐉'
admin.site.site_header = 'Dragons 🐉'
admin.site.site_title = "TODO_LIST_APP 🦅 "