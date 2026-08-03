from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (

        (
            "Library Information",

            {
                "fields": (
                    "phone",
                    "address",
                    "is_librarian",
                    "is_admin",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
        "is_librarian",
        "is_admin",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )

    list_filter = (
        "is_admin",
        "is_librarian",
        "is_staff",
        "is_active",
    )


# Register your models here.
