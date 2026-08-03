from django.contrib import admin
from .models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "book",
        "borrow_date",
        "is_returned",
    )

    list_filter = (
        "is_returned",
        "borrow_date",
    )

    search_fields = (
        "user__username",
        "book__title",
    )

# Register your models here.
