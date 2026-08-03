from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import RegisterForm, EditProfileForm
from .models import CustomUser


# ==========================
# Register
# ==========================

def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("login")

        else:
            print("=" * 50)
            print(form.errors)
            print("=" * 50)

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )



# ==========================
# Login
# ==========================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.is_superuser or user.is_admin:
                return redirect("admin_dashboard")

            return redirect("book_list")

        else:

            messages.error(
                request,
                "Username or Password is incorrect."
            )

    return render(
        request,
        "accounts/login.html"
    )


# ==========================
# Logout
# ==========================

def logout_view(request):

    logout(request)

    return redirect("login")


# ==========================
# Profile
# ==========================

@login_required
def profile_view(request):

    return render(
        request,
        "accounts/profile.html"
    )


# ==========================
# Edit Profile
# ==========================

@login_required
def edit_profile(request):

    if request.method == "POST":

        form = EditProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile")

    else:

        form = EditProfileForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "form": form
        }
    )


# ==========================
# Change Password
# ==========================

@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("profile")

    else:

        form = PasswordChangeForm(
            request.user
        )

    return render(
        request,
        "accounts/change_password.html",
        {
            "form": form
        }
    )


# ==========================
# Admin Dashboard
# ==========================

@login_required
def admin_dashboard(request):

    if not (
        request.user.is_superuser
        or request.user.is_admin
    ):

        return redirect("book_list")

    return render(
        request,
        "accounts/admin_dashboard.html"
    )


# ==========================
# Manage Users
# ==========================

@login_required
def manage_users(request):

    if not (
        request.user.is_superuser
        or request.user.is_admin
    ):

        return redirect("book_list")

    users = CustomUser.objects.all()

    return render(
        request,
        "accounts/manage_users.html",
        {
            "users": users
        }
    )
# Create your views here.
