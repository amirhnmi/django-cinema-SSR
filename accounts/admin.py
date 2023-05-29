from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display=["id","email","username","first_name","last_name","phone_number","is_staff","is_superuser","is_active"]
    ordering = ["id"]
    list_filter=["is_staff","is_active","email"]
    fieldsets=(
        ("User information",{"fields":("email","password","username")}),
        ("Permissions", {"fields":("is_staff","is_active","groups","user_permissions")}),
    )
    add_fieldsets=(
        ("create user",{
            "classes":("wide",),
            "fields":(
                "email","username","password1","password2","is_staff","is_active","groups","user_permissions"
            )}
        ),
    )


admin.site.register(CustomUser,CustomUserAdmin)
