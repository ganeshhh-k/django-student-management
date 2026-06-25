from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request, username=username, password=password
        )

        if user:
            auth_login(request, user)
            return redirect('/')
    return render(
        request, 'login.html'
    )

def logout_user(request):
    logout(request)

    return redirect('/accounts/login/')