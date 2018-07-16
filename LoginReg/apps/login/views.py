from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import User

def index(request):
    return render(request, 'login/index.html')

def register(request):
    error = User.objects.validator(request.POST)
    if (errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('register:index')

    return redirect('register:success')

def login(request):
    if (User.objects.filter(username=request.POST['login_user']).exists()):
        user = User.objects.filter(username=request.POST['username'])
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('list_wish:index')
    return redirect('register:index')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user
    }
    return render(request, 'login:success.html', context)

def logout(request):
    request.session.clear()
    return redirect('logout:index')




# Create your views here.
