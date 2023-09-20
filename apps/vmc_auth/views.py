"""Item auth views."""
from typing import Any, Dict

from django.forms.models import BaseModelForm
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.views.generic import FormView, DeleteView  # , TemplateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignupForm, SigninForm
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy

# from django.dispatch import receiver

# from django.utils.translation import gettext_lazy as _
from apps.vmc_auth.models import User

from config import settings
from apps.vmc.forms import MessageForm


def signup(request):
    """Signup view."""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(
                request, user, backend="apps.vmc_auth.authenticate.EmailModelBackend"
            )
            return redirect("vmc_sandbox:todolist")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})


def signin(request):
    """Signin view."""
    if request.method == "POST":
        form = SigninForm(None, request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            auth_login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return redirect("vmc_sandbox:todolist")
    else:
        form = SigninForm()
    return render(
        request,
        "registration/signin.html",
        {"form": form},
    )


class LoginView(LoginView):
    template_name = "registration/signin.html"
    form_class = SigninForm

    def post(self, request, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            auth_login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return redirect("vmc_sandbox:todolist")

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())


class ProfileView(LoginRequiredMixin, FormView):
    """Profile view."""

    template_name: str = "registration/profile.html"
    form_class = MessageForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "slogan": settings.SLOGAN,
                "myaccount": settings.MYACCOUNT,
                "profile": settings.PROFILE,
                "mailbox": settings.MAILBOX,
                "logout": settings.LOGOUT,
            }
        )
        return context


class DeleteAccount(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/user_confirm_delete.html"
    success_url = reverse_lazy("vmc_sandbox:index")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object.id)

        if self.object.id == self.request.user.id:
            self.object.delete()
            return redirect(self.success_url)
        return self.render_to_response(context)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Form valid."""
        self.object = self.get_object()
        msg = f"The account: {self.object.title} was successfully deleted."
        self.object.delete()
        return HttpResponse(status=204, headers={"Msg-Status": msg})

    # def render_to_response(self, context, **response_kwargs):
    #     if self.get_object() != self.request.user:
    #         messages.success(
    #             self.request,
    #             mark_safe(
    #                 "Cette action n'est pas possible.\
    #                     Le compte que tu cherches à supprimer n'existe pas."
    #             ),
    #         )
    #         return redirect("index")
    #     messages.success(
    #         self.request,
    #         mark_safe("Le compte à bien été supprimé."),
    #     )
    #     return super().render_to_response(context)


def user_logout(request):
    """Log out."""
    logout(request)
    return redirect("vmc_sandbox:index")
