"""Model Admin."""
from django.contrib import admin
from .models import Item, Thread, Message


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin class.

    This class is needed only for customize purpose. Without custom :
    admin.site.register(Item) will suffice.
    """

    list_display = ["title", "task", "format_date"]

    fieldsets = [
        # Allow to show only those fields in admin to create a new entry.
        # By default, we would see the is_task_done field.
        (
            None,
            {
                "fields": ["title", "task", "date"],
            },
        ),
    ]


class ThreadAdmin(admin.ModelAdmin):
    """Thread Admin class."""

    list_display = ["title", "sender", "get_receivers"]

    fieldsets = [
        (
            None,
            {
                "fields": ["title", "sender", "receiver"],
            },
        ),
    ]

    def get_receivers(self, obj):
        """Get receivers from ManyToManyField."""
        return ", ".join([user.username for user in obj.receiver.all()])


admin.site.register(Thread, ThreadAdmin)


class MessageAdmin(admin.ModelAdmin):
    """Message Admin class."""

    list_display = ["msg_content", "date_time"]

    fieldsets = [
        (
            None,
            {
                "fields": ["msg_content", "date_time"],
            },
        ),
    ]


admin.site.register(Message, MessageAdmin)
