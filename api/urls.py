
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
  path('api/', include(router.urls)),
]

