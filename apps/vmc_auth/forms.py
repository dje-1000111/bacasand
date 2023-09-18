"""Item Auth forms."""
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate

UserModel = get_user_model()
# from EmailModelBackend import authenticate


class UserCreationForm(auth_forms.UserCreationForm):
    """User creation form class."""

    class Meta(auth_forms.UserCreationForm.Meta):
        """User creation form meta class."""

        model = get_user_model()


class SignupForm(auth_forms.UserCreationForm):
    """Inscription form."""

    email = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "off",
                "class": "form-control me-2",
                "input_type": "email",
                "placeholder": _("e.g. user@mailbox.com"),
                "data-email": "",
            }
        ),
    )
    username = forms.CharField(
        label=_("Username"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "Pseudo",
            }
        ),
    )
    password1 = forms.CharField(
        label=_("Password"),
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control me-2",
                "input_type": "password",
            }
        ),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control me-2",
                "input_type": "password",
            }
        ),
    )

    class Meta:
        """InscriptForm meta class."""

        model = get_user_model()
        fields = ("username", "email", "password1", "password2")


class SigninForm(auth_forms.AuthenticationForm):
    """Login form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.invalid_login = ""
        for field in self.fields.values():
            field.error_messages = {
                "required": _("The {fieldname} field is required.").format(
                    fieldname=field.label
                ),
                "invalid_login": _("Please enter a correct email and password."),
            }

        self.invalid_login = [field.error_messages for field in self.fields.values()][
            0
        ]["invalid_login"]

    email = forms.EmailField(
        label=_("Email"),
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": _("e.g. user@mailbox.com"),
                "data-email": "",
            }
        ),
    )

    password = forms.CharField(
        label=_("Password"),
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "",
            }
        ),
    )

    class Meta:
        """LoginForm meta class."""

        model = get_user_model()
        fields = ("email", "password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        div, err = "", ""

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                return cleaned_data
            else:
                # Simulate errorlist to fit with post_form_signin.js
                # err = "L'email ou le Mot de passe ne correspondent pas !"
                err = self.invalid_login
                div = f'<div class="errorlist alert alert-danger mt-3">{err}</div>'
        raise forms.ValidationError(mark_safe(div))
