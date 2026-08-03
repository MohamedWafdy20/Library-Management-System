from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from catalog.models import Book
from .models import Loan


@login_required
def borrow_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if book.available_copies <= 0:

        messages.error(
            request,
            "No copies available."
        )

        return redirect("book_list")

    
    already_borrowed = Loan.objects.filter(
        user=request.user,
        book=book,
        is_returned=False
    ).exists()

    if already_borrowed:

        messages.error(
            request,
            "You already borrowed this book."
        )

        return redirect("book_list")

    Loan.objects.create(
        user=request.user,
        book=book
    )

    book.available_copies -= 1
    book.save()

    messages.success(
        request,
        "Book borrowed successfully."
    )

    return redirect("book_list")


@login_required
def return_book(request, loan_id):

    loan = get_object_or_404(
        Loan,
        id=loan_id,
        user=request.user
    )

    if loan.is_returned:

        messages.error(
            request,
            "This book has already been returned."
        )

        return redirect("my_loans")

    loan.is_returned = True
    loan.save()

    book = loan.book
    book.available_copies += 1
    book.save()

    messages.success(
        request,
        "Book returned successfully."
    )

    return redirect("my_loans")


@login_required
def my_loans(request):

    loans = Loan.objects.filter(
        user=request.user,
        is_returned=False
    )

    return render(
        request,
        "loans/my_loans.html",
        {
            "loans": loans
        }
    )
# Create your views here.
