from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):
    pass
    
   #model = User
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    
   




admin.site.register(User, UserAdmin)
