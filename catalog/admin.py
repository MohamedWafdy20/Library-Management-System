from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish_year', 'avilable_copies', 'isbn','total_copies')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('category', 'publish_year')

# Register your models here.
