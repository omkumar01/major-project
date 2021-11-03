from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import View


class LoginRegister(View):

    def get(self, request):
        return render(request, 'LoginRegister.html')

    def post(self, request):
        context = {}
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('user logged in')
            return redirect('/')

        else:
            context = {
                'login': False,
                'message': 'Invalid username or password'
            }
            print("login failed")
            return render(request, 'LoginRegister.html', context)


class Logout(LoginRegister):

    def get(self, request):
        logout(request)
        return redirect('/LoginRegister')


class ChangePassowrd(View):
    def get(self, request):
        return render(request, "changePassword.html")

    def post(self, request):
        content = {}
        if request.POST['username']:
            username = request.POST['username']
            user = User.objects.get(username=username)

            if user is None:
                content['message'] = 'User not found'
                return render(request, "changePassword.html", content)

            else:
                content['user'] = username
                return render(request, "changePassword.html", content)

        username = request.POST['name']
        password = request.POST['password']

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        return redirect('/LoginRegister')


class Register(LoginRegister):

    def get(self, request):
        return redirect('/LoginRegister')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        try:
            add_user = User.objects.create_user(
                first_name=name,
                username=email,
                email=email,
                password=password,
                is_superuser=False,
            )
            add_user.save()

        except:
            return HttpResponse('task failed sucessfully')

        return redirect('LoginRegister/')
