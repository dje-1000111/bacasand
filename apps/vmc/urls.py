"""Urls vmc."""
from django.urls import path

from apps.vmc import views

app_name = "vmc_sandbox"

urlpatterns = [
    path("", views.index, name="index"),
    path("app/", views.ReadList.as_view(), name="todolist"),
    path("app/items", views.item_list, name="item_list"),
    path("app/item/<int:pk>/delete", views.DeleteItem.as_view(), name="delete_item"),
    path("ajax_url_done/", views.save_done_chkbx, name="is_done"),
    path("app/item/<int:pk>/edit", views.UpdateItem.as_view(), name="update_form"),
    path("app/item/new", views.CreateItem.as_view(), name="create_form"),
    path(
        "mailbox/",
        views.ThreadList.as_view(),
        name="mailbox_thread",
    ),
    path(
        "mailbox/thread/<int:thread_id>/msg/",
        views.MessageList.as_view(),
        name="mailbox_msgs",
    ),
    path(
        "mailbox/thread/<int:thread_id>/msg/response/",
        views.msg_response,
        name="msg_response",
    ),
    path("mailbox/new/", views.create_message, name="create-msg"),
    path(
        "mailbox/thread/<int:thread_id>/msg/<int:msg_id>/",
        views.delete_message,
        name="delete-msg",
    ),
    path("mailbox/new/thread/", views.create_thread, name="create-thread"),
    path("mailbox/thread/<int:thread_id>/", views.delete_thread, name="delete_thread"),
]
