from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name