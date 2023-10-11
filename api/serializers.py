# serializers.py

from rest_framework import serializers
from myApp.models import Blog, Company, Category, Tag

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'




# from rest_framework import viewsets
# from .models import Blog, Company, Category, Tag
# from .serializers import BlogSerializer, CompanySerializer, CategorySerializer, TagSerializer

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
