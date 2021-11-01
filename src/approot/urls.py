from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chatapp.urls")),
    # authentication urls
    path('LoginRegister/', LoginRegister.as_view(), name='login'),
    path('register', Register.as_view()),
    path('logout/', Logout.as_view()),
    path('changepassword/', ChangePassowrd.as_view()),
]
