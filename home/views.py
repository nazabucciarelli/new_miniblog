from django.contrib.auth import (
    authenticate,
    login)
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.views import View
# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(
            request,
            'index/login.html'
        )
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username = username,
                password = password
            )
            if user:
                print(user)
                login(request,user)
                return redirect('index')
        return redirect('login')

@login_required(login_url="/login/")
def index_view(request):
    return render(
        request,
        'index/index.html'
    )
