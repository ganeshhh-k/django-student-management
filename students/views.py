from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()

    return render(request, 'home.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = StudentForm()

    return render(
        request, 'add_student.html', {'form': form}
    )

@login_required
def update_student(request, id):
    student = Student.objects.get(id=id)
    
    if request.method == 'POST':
        form = StudentForm(
            request.POST, instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = StudentForm(
            instance=student
        )

    return render(request, 'add_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')