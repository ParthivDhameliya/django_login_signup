from django.shortcuts import render, HttpResponseRedirect
from .forms import userLogin, userSignup
from .models import registrationModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'user/home.html')


def user_signup(request):
    if request.method == 'POST':
        form = userSignup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congretulations, You registered successfully!!')
            return HttpResponseRedirect('/login/')
    else:
        form = userSignup()
    return render(request, 'user/signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = userLogin(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!!')
                    return HttpResponseRedirect('/profile/')
        else:
            form = userLogin()
        return render(request, 'user/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'user/profile.html')
    else:
        return HttpResponseRedirect('/login/')


def user_changepassword(request):
    return render(request, 'user/changepassword.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
