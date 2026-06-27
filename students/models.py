from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    semester = models.IntegerField()
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="students/", blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"