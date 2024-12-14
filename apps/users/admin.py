from django.contrib import admin

# Register your models here.
 
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Specify which fields to display in the admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),  # Add any additional fields here
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),  # Add any additional fields here
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'organization', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
