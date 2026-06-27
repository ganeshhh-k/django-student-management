from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

def home(request):
    students = Student.objects.all()

    total_students = students.count()
    active_students = students.filter( active = True).count()
    inactive_students = students.filter( active = False).count()
    total_branches = Student.objects.values("branch").distinct().count()

    search = request.GET.get("search")
    if search:
        students = students.filter(
            Q(name__icontains=search) | Q(roll_no__icontains=search)
        )

    branch = request.GET.get("branch")
    if branch:
        students = students.filter(branch=branch)

    semester = request.GET.get("semester")
    if semester:
        students = students.filter(semester = semester)

    status = request.GET.get("status")

    if status == "active":
        students = students.filter(active=True)

    elif status == "inactive":
        students = students.filter(active=False)

    sort = request.GET.get("sort")
    if sort:
        students = students.order_by(sort)

    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'home.html', {"students": students,
                                         "total_students": total_students,
                                         "active_students": active_students,
                                         "inactive_students": inactive_students,
                                         "total_branches": total_branches})
                            

@login_required
def add_student(request):
    if request.method == 'POST':
        roll_no = request.POST['roll_no']
        name = request.POST['name']
        branch = request.POST['branch']
        semester = request.POST['semester']
        active = request.POST.get("active") == "True"
        photo = request.FILES.get("photo")

        if Student.objects.filter(roll_no = roll_no).exists():
            return render(request, "add_student.html", {"error": "Roll no already exists"})

        Student.objects.create(
            roll_no = roll_no,
            name = name,
            branch = branch,
            semester = semester,
            active = active,
            photo = photo
        )
        messages.success(request, "Student added Successfully!")
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
            messages.success(request, "Student Updated successfully!")
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
    messages.warning(request, "Student deleted successfully!")

    return redirect('/')

def student_profile(request, id):
    student = get_object_or_404(Student, id=id)

    return render(
        request, "student_profile.html", {"student": student}
    )