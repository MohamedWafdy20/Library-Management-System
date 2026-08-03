from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Authentication
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    # Profile
    path("profile/", views.profile_view, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),

    # Forgot Password
    path(
        "forgot-password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/forgot_password.html"
        ),
        name="forgot_password",
    ),

    path(
        "forgot-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/forgot_password_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    # Admin
    path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "manage-users/",
        views.manage_users,
        name="manage_users"
    ),
]