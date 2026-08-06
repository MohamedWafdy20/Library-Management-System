from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.help_text = ""
            field.widget.attrs.update({"class": "form-control"})

        self.fields["username"].widget.attrs.update({"placeholder": "Username"})
        self.fields["email"].widget.attrs.update({"placeholder": "Email"})
        self.fields["first_name"].widget.attrs.update({"placeholder": "First Name"})
        self.fields["last_name"].widget.attrs.update({"placeholder": "Last Name"})
        self.fields["phone"].widget.attrs.update({"placeholder": "Phone Number"})
        self.fields["address"].widget.attrs.update({"placeholder": "Address"})

        if "password1" in self.fields:
            self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Password"})
        if "password2" in self.fields:
            self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Confirm Password"})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email


class EditProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })
        