from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Blog, Company, Category, Tag
from .serializers import BlogSerializer, CompanySerializer, CategorySerializer, TagSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    @action(detail=True, methods=['DELETE'])
    def delete_blog(self, request, pk=None):
        try:
            blog = self.get_object()
            blog.delete()
            return Response(status=204)  
        except Blog.DoesNotExist:
            return Response(status=404)  
        
    @action(detail=True, methods=['PUT'], serializer_class=BlogSerializer)
    def update_blog(self, request, pk=None):
        try:
            blog = self.get_object()
            serializer = self.get_serializer(blog, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response(status=404) 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


