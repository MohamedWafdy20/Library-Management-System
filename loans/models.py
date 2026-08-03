from django.db import models
from django.conf import settings
from catalog.models import Book


class Loan(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    borrow_date = models.DateTimeField(auto_now_add=True , editable=False)

    return_date = models.DateTimeField(
        null=True,
        blank=True
    )

    is_returned = models.BooleanField(default=False)

    class Meta:
        ordering = ['-borrow_date']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

# Create your models here.
