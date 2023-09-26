from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView ,DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class ModelListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class CreateBlog(CreateView):
    model = Post
    template_name= 'post_new.html'
    fields = ['author','title','content']
    success_url = reverse_lazy('home')
    
    
class UpdateViewBlog(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','content']
    success_url = reverse_lazy('home')
    
class DeleteViewBlog(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')