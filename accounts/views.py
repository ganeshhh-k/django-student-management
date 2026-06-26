from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:

            return render(
                request,
                'register.html',
                {'error': 'Passwords do not match'}
            )

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'register.html',
                {'error': 'Username already exists'}
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/accounts/login/')

    return render(request, 'register.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(
                request, 'login.html', {'error': 'Invalid Credientials'}
            )
    return render(
        request, 'login.html'
    )

def logout_user(request):
    logout(request)

    return redirect('/accounts/login/')