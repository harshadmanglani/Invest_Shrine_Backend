from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, Category

class UserAdmin(admin.ModelAdmin):
    
    #fields = ["category",]
    pass
    



admin.site.register(User, UserAdmin)
admin.site.register(Category)