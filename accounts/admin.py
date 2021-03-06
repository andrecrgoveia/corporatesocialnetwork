# Djangos' imports
from django.contrib import admin

# Developer's imports
from django.contrib.auth.admin import UserAdmin

# Forms' imports
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Models' imports
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        'first_name',
        'last_name',
        'user_image',
        "id",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    'first_name',
                    'last_name',
                    'user_image',
                    "password",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    'first_name',
                    'last_name',
                    'user_image',
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
