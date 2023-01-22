from .views import *
from django.urls import path, include
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path("accounts/signup", registro, name="registro"),
    path("accounts/login", login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]