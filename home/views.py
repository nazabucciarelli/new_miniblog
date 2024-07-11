from django.contrib.auth import (
    authenticate,
    login,
    logout)
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import View
from user.forms import UserRegisterForm

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

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'index/register.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form':form
            }  
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'form':form
            }
        )

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

@login_required(login_url="/login/")
def index_view(request):
    return render(
        request,
        'index/index.html'
    )
