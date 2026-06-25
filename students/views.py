from django.shortcuts import render

def home(request):
    students = [
        {'name' : 'Ganesh', 'branch': 'CSE', 'active': True},
        {'name' : 'Ravi', 'branch': 'ECE', 'active': True},
        {'name' : 'Raju', 'branch': 'EEE', 'active': False},
    ]
    return render(request, 'home.html', {'students': students})
