from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    semester = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name