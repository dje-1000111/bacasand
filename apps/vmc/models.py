"""SandBox Models."""
from typing import Any, Dict
from django.utils import timezone
from django.contrib import admin
from django.db import models
from config import settings


class Item(models.Model):
    """Item Class."""

    title = models.CharField(max_length=50)
    task = models.TextField(max_length=255)
    date = models.DateField(max_length=8)
    is_done = models.BooleanField("is_task_done", default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> Any:
        """Str."""
        return super().__str__()

    class Meta:
        """Ordering by date."""

        ordering = ["-date", "is_done"]

    @admin.display
    def format_date(self):
        """Format date.

        Allow to show the date formated like that: dd/mm/yyyy
        """
        return self.date.strftime("%d/%m/%Y")


class Thread(models.Model):
    """Thread."""

    title = models.CharField(max_length=50)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="thread_sender",
        on_delete=models.CASCADE,
    )
    receiver = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="thread_receiver",
    )
    email_choices = models.CharField(max_length=254)


class Message(models.Model):
    """Message Item."""

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sender",
        on_delete=models.CASCADE,
    )
    receiver = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="receiver")
    msg_content = models.TextField("message", max_length=255)
    created_at = models.DateTimeField(
        default=timezone.now,
    )
    thread = models.ForeignKey(
        Thread,
        related_name="thread_id",
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return f"<Message {self.msg_content}>"

    @admin.display
    def date_time(self):
        """Format date.

        Allow to show the date formated like that: dd/mm/yyyy h:m:s
        """
        return self.created_at.strftime("%d/%m/%Y %H:%M:%S")
