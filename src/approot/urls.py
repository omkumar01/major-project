from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login-register", include("loginregister.urls"), name="loginregister"),
    path("", include("chatapp.urls"), name="chatapp"),
]
