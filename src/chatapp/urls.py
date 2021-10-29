from django.contrib import admin
from django.urls import path
from .views import ChatApp

urlpatterns = [
    path("", ChatApp.as_view() ),
]