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
        roll_no = request.POST['roll_no']
        name = request.POST['name']
        branch = request.POST['branch']
        semester = request.POST['semester']
        active = 'active' in request.POST

        if Student.objects.filter(roll_no = roll_no).exists():
            return render(request, "add_student.html", {"error": "Roll no already exists"})

        Student.objects.create(
            roll_no = roll_no,
            name = name,
            branch = branch,
            semester = semester,
            active = active
        )
        return redirect('/')

    return render(
        request, 'add_student.html')

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

    return render(request, 'update_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')