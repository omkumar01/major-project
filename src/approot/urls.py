from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login-register", TemplateView.as_view(template_name="login_register.html"),
         name="loginregister"),
    path("", include("chatapp.urls"), name="chatapp"),
    path("accounts/", include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]
