from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Book Title")
    author = models.CharField(max_length=100, verbose_name="Author Name")
    isbn = models.CharField(max_length=13, unique=True,)
    category = models.CharField(max_length=50, verbose_name="Category")
    publish_year = models.IntegerField(verbose_name="Publish Year")
    available_copies = models.PositiveIntegerField(default=1, verbose_name="Avilable Copies")
    total_copies = models.PositiveIntegerField(default=1, verbose_name="Total Copies")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.title

# Create your models here.
