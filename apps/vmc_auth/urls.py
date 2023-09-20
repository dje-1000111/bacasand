"""Auth urls."""
from django.urls import path
from apps.vmc_auth import views

app_name = "auth"

urlpatterns = [
    path("accounts/signup/", views.signup, name="signup"),
    # path("accounts/signin/", views.signin, name="signin"),
    path("accounts/signin/", views.LoginView.as_view(), name="signin"),
    path("accounts/signin/#signin-modal", views.signin, name="signin_modal"),
    path("accounts/profile/", views.ProfileView.as_view(), name="profile"),
    path("accounts/signout", views.user_logout, name="signout"),
    path(
        "accounts/profile/delete/<int:pk>/",
        views.DeleteAccount.as_view(),
        name="delete_account",
    ),
]
