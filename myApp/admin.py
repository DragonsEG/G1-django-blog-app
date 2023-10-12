from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

## To Show automatically handled fields in admin site
# Automatic handled fields like auto_now and auto_now_add
# By default, these automatically handled fields are not shown in the admin site 
# while creating or editing a record. 
# You can show them by making them readonly fields

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(UserProfile)
admin.site.register(JoinRequest)
admin.site.register(Company)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)

#ahmedreda
#ahmed@gmail.com
#admin