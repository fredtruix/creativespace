from django.shortcuts import redirect, render
from .models import  User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import (UserRegisterForm,
 ProfileUpdateForm)
from base.models import Topic
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



# Create your views here.

def RegisterView(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'users/login_register.html', {"form":form})


def LoginView(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Username or password does not exist')
 
    context = {"login":page}
    return render(request, 'users/login_register.html', context)


def ProfileView(request, name):
    user = User.objects.get(username=name)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()[0:5]
    p = Paginator(rooms, 1)
    page = request.GET.get('page')
    rooms = p.get_page(page)
    context = {
        'user':user,
        'rooms':rooms,
        'room_messages':room_messages,
        'topics':topics,
        }
    return render(request, 'users/profile.html', context)


def ProfileUpdateView(request):
    user = request.user
    form = ProfileUpdateForm(instance=user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user)
    return render(request, 'users/user_update.html', {'form':form})


def LogoutView(request):
    logout(request)
    return redirect('home')



