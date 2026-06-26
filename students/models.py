from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    semester = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"