from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'pk']
    list_filter = ['email', 'username', 'last_name', 'is_superuser']
    search_fields = ['email', 'username', 'first_name']
    date_hierarchy = 'created'
    ordering = ['is_active', 'email']