from django.shortcuts import render
from django.views.generic import View


class ChatApp(View):
    def get(self, request):
        context = {}
        return render(request, "index.html", context)
