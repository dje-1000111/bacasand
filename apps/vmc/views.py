"""Item vmc views."""
import json
from typing import Any, Dict
from django.db.models import Q
from django.forms.models import BaseModelForm
from apps.vmc_auth.models import User
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.urls import reverse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from apps.vmc.models import Item, Message, Thread
from apps.vmc.forms import ItemForm, MessageForm, ThreadForm
from config import settings

nav = {
    "slogan": settings.SLOGAN,
    "myaccount": settings.MYACCOUNT,
    "profile": settings.PROFILE,
    "mailbox": settings.MAILBOX,
    "logout": settings.LOGOUT,
}


def error_404(request: HttpRequest, exception) -> HttpResponse:
    """Error 404 view."""
    return render(request, "pages/404.html", status=404)


def index(request: HttpRequest) -> HttpResponse:
    """Index."""
    pres1 = _(
        "is an online boot camp (a sandbox) which aims to approach the "
        "constraints of creation and maintenance in real conditions as part of a "
        "deployment continuous."
    )
    pres2 = _("The techs used are:")
    pres3 = _("The app will evolve as different features are added.")
    context = {
        "pres1": pres1,
        "pres2": pres2,
        "pres3": pres3,
        "signup": settings.SIGNUP,
        "login": settings.LOGIN,
    }
    context.update(nav)
    return render(request, "pages/index.html", context)


class CreateItem(LoginRequiredMixin, CreateView):
    """Create Item View.

    As specified here :
    https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic
    -editing/#models-and-request-user
    """

    template_name: str = "pages/create_form.html"
    model = Item
    form_class = ItemForm

    # LoginRequiredMixin
    redirect_field_name = settings.LOGIN_URL
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "create_form": context.get("form"),
            }
        )
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Form valid."""
        form.instance.user_id = self.request.user.pk
        self.object = form.save()
        msg = f"Object title: {self.object.title} was successfully created."
        return HttpResponse(status=204, headers={"Msg-Status": msg})

    def get_success_url(self) -> str:
        """Get success url."""
        return reverse("vmc_sandbox:create_form")


class ReadList(LoginRequiredMixin, ListView):
    """Read List View."""

    template_name: str = "pages/read_list.html"
    model = Item

    # LoginRequiredMixin
    redirect_field_name = settings.LOGIN_URL
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Get context data."""
        context = super().get_context_data(**kwargs)
        title_heads = [
            _("Status"),
            _("Title"),
            _("Task"),
            _("Date"),
            _("Edit"),
            _("Del"),
        ]
        context.update(nav)
        context.update(
            {
                "title_heads": title_heads,
                "modal_create_title": settings.MODAL_CREATE_TITLE,
                "modal_update_title": settings.MODAL_UPDATE_TITLE,
                "modal_delete_title": settings.MODAL_DELETE_TITLE,
                "cancel": settings.CANCEL,
                "submit": settings.SUBMIT,
            }
        )
        return context


def save_done_chkbx(request: HttpRequest) -> JsonResponse:
    """Save as done task from ajax post."""
    data = json.loads(request.body)
    status = data["status"]
    item_id = data["item_id"]

    item = Item.objects.get(pk=item_id)
    if status:
        item.is_done = True
    else:
        item.is_done = False
    item.save()
    return JsonResponse({"result": "done"}, safe=False)


def item_list(request: HttpRequest) -> HttpResponse:
    """Populate the item list."""
    return render(
        request,
        "pages/list.html",
        {
            "item_list": Item.objects.all(),
        },
    )


class UpdateItem(LoginRequiredMixin, UpdateView):
    """Update Item View.

    Initial printing from URL.
    """

    template_name: str = "pages/update_form.html"
    model = Item
    form_class = ItemForm

    # LoginRequiredMixin
    redirect_field_name = settings.LOGIN_URL
    login_url = settings.LOGIN_URL

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """If the form is valid, save the associated model."""
        item = Item.objects.get(pk=self.kwargs["pk"])
        self.object = form.save()
        if item.is_done:
            self.object.is_done = True
        msg = f"Object title: {self.object.title} was successfully updated."
        return HttpResponse(status=204, headers={"Msg-Status": msg})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context["update_form"] = context.get("form")
        context.update(
            {
                "update_form": context.get("form"),
            }
        )
        return context

    def get_success_url(self) -> str:
        """Get success url."""
        return reverse("vmc_sandbox:update_form", kwargs={"pk": self.kwargs["pk"]})


class DeleteItem(LoginRequiredMixin, DeleteView):
    """Delete View."""

    template_name: str = "pages/delete_object.html"
    model = Item
    success_url = reverse_lazy("vmc_sandbox:index")

    # LoginRequiredMixin
    redirect_field_name = settings.LOGIN_URL
    login_url = settings.LOGIN_URL

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Form valid."""
        self.object = self.get_object()
        msg = f"Item title: {self.object.title} was successfully deleted."
        self.object.delete()
        return HttpResponse(status=204, headers={"Msg-Status": msg})


class MessageList(LoginRequiredMixin, ListView):
    """Message list."""

    template_name: str = "pages/mailbox.html"
    model = Message

    # LoginRequiredMixin
    redirect_field_name = settings.LOGIN_URL
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Get context data."""
        object_list = self.model.objects.filter(
            Q(sender_id=self.request.user.pk) | Q(receiver=self.request.user),
            thread_id=self.kwargs["thread_id"],
        )
        context = super().get_context_data(**kwargs)
        context["msg_list"] = object_list
        context["thread_id"] = self.kwargs["thread_id"]
        context.update(nav)
        return context


class ThreadList(LoginRequiredMixin, ListView):
    """Message list."""

    template_name: str = "pages/mailbox.html"
    model = Thread

    # LoginRequiredMixin
    redirect_field_name = settings.LOGIN_URL
    login_url = settings.LOGIN_URL

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Get context data."""
        object_list = self.model.objects.filter(
            Q(sender_id=self.request.user.pk) | Q(receiver=self.request.user)
        )
        context = super().get_context_data(**kwargs)
        # Note: the set(object_list) is needed to avoid duplicate querysets.
        context["thread_list"] = list(set(object_list))
        context["all_msg"] = Message.objects.all()
        context.update(nav)
        return context


@login_required(redirect_field_name=settings.LOGIN_URL, login_url=settings.LOGIN_URL)
def create_message(request: HttpRequest):
    """Create message."""
    if request.method == "POST":
        form = MessageForm(request.POST)
        thread = Thread.objects.all().last()
        users = User.objects.filter(pk__in=[i.pk for i in thread.receiver.all()])
        if form.is_valid():
            msg = Message.objects.create(
                msg_content=request.POST.get("msg_content"),
                sender=request.user,
                thread_id=thread.pk,
            )
            msg.receiver.set([i for i in users.all()])
            return redirect("vmc_sandbox:mailbox_thread")
    else:
        form = MessageForm()
    context = {"form": form}
    return render(request, "pages/message_form.html", context)


@login_required(redirect_field_name=settings.LOGIN_URL, login_url=settings.LOGIN_URL)
def create_thread(request):
    """Create thread."""
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            users = User.objects.filter(email__in=request.POST.getlist("email_choices"))
            thread = Thread.objects.create(
                title=request.POST.get("title"),
                sender=request.user,
            )
            thread.receiver.set(users)

            return redirect("vmc_sandbox:create-msg")
    else:
        form = ThreadForm()
    context = {"form": form}
    context.update(nav)
    return render(request, "pages/thread.html", context)


@login_required(redirect_field_name=settings.LOGIN_URL, login_url=settings.LOGIN_URL)
def msg_response(request, thread_id):
    """Message response."""
    thread = Thread.objects.get(pk=thread_id)
    users = User.objects.filter(pk__in=[i.pk for i in thread.receiver.all()])
    if request.method == "POST":
        form = MessageForm(request.POST)
        msg = Message.objects.create(
            msg_content=request.POST.get("msg_content"),
            sender=request.user,
            thread_id=thread_id,
        )
        msg.receiver.set([i for i in users.all()])
        return redirect("vmc_sandbox:mailbox_msgs", thread_id=thread_id)
    else:
        form = MessageForm()
    context = {"form": form, "thread_id": thread_id}
    context.update(nav)
    return render(
        request,
        "pages/message_form.html",
        context,
    )


@login_required(redirect_field_name=settings.LOGIN_URL, login_url=settings.LOGIN_URL)
def delete_message(request, thread_id, msg_id):
    """Delete message."""
    msg = Message.objects.get(pk=msg_id)
    if (
        msg.sender == request.user
        and msg.sender.is_staff
        and msg.sender.is_authenticated
    ):
        msg.delete()
    return redirect("vmc_sandbox:mailbox_msgs", thread_id=thread_id)


@login_required(redirect_field_name=settings.LOGIN_URL, login_url=settings.LOGIN_URL)
def delete_thread(request, thread_id):
    """Delete thread."""
    thread = Thread.objects.get(pk=thread_id)
    if thread.sender == request.user:
        thread.delete()

    return redirect("vmc_sandbox:mailbox_thread")
