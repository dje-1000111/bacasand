"""Forms."""
from datetime import datetime as dt

from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm, DateInput

from apps.vmc_auth.models import User
from .models import Item, Thread, Message
from config import settings


class CustomDateInput(DateInput):
    """Date input."""

    input_type = "date"


class ItemForm(ModelForm):
    """Item Form."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.fields["is_done"].widget.attrs.update(
            {
                "class": "btn btn-primary",
                "name": "is-done",
            }
        )
        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control mt-3 mb-2 w-75 centerize",
                "placeholder": settings.FORM_PLACEHOLDER_TITLE,
                "name": "title",
                "autocomplete": "off",
                "id": "title",
            }
        )
        self.fields["task"].widget.attrs.update(
            {
                "class": "form-control mb-2 w-75 centerize",
                "placeholder": settings.FORM_PLACEHOLDER_CONTENT,
                "cols": 20,
                "rows": 5,
                "name": "task",
                "autocomplete": "off",
            }
        )
        self.fields["date"].widget.attrs.update(
            {
                "class": "form-control mb-2 w-75 centerize",
                "name": "date",
                "id": "date",
            }
        )

    class Meta:
        """Meta."""

        model = Item
        fields = {"is_done": "", "title": "", "task": "", "date": ""}  # "__all__"
        labels = {"is_done": "", "title": "", "task": "", "date": ""}

        # For recall, to show the current date in the input (instead of dd/mm/yyyy),
        # the VALID format in value should be %Y-%m-%d.
        # With another type of format, it's just "dd/mm/yyyy" !!!
        widgets = {
            "date": CustomDateInput(attrs={"value": dt.now().strftime("%Y-%m-%d")}),
        }

    def clean_date(self):
        """Return cleaned date."""
        date = self.cleaned_data["date"]
        if (
            dt.now().year - 1 < date.year <= dt.now().year + 1
            and 0 < date.month < 13
            and 0 < date.day < 32
        ):
            return date
        raise ValidationError(
            "Cette entrée est invalide. La valeur attendue\
             est une date à partir de l'année en cours (+ 1 an max).",
        )


class ThreadForm(ModelForm):
    """Thread form."""

    class Meta:
        """Meta."""

        model = Thread
        fields = {"title": "", "email_choices": ""}
        labels = {
            "title": "Titre de la discussion",
            "email_choices": "Sélectionnez le ou les destinataires",
        }
        staff_users = User.objects.filter(is_staff=True).order_by("username")
        # /!\ Deactivate this two lines before makemigrations
        # EMAIL_CHOICES = [(user.email, user.email) for user in staff_users]
        # if EMAIL_CHOICES:
        #     widgets = {
        #         "email_choices": forms.SelectMultiple(choices=EMAIL_CHOICES),
        #     }


class MessageForm(ModelForm):
    """Message form."""

    class Meta:
        """Meta."""

        model = Message
        fields = {"msg_content": ""}
        labels = {
            "msg_content": "Saississez votre message",
        }
        widgets = {
            "msg_content": forms.Textarea(),
        }
