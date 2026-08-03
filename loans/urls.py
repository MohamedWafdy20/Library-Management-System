from django.urls import path
from . import views

urlpatterns = [

    path(
        "borrow/<int:book_id>/",
        views.borrow_book,
        name="borrow_book"
    ),

    path(
        "return/<int:loan_id>/",
        views.return_book,
        name="return_book"
    ),

    path(
        "my-loans/",
        views.my_loans,
        name="my_loans"
    ),

]