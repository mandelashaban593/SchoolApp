from django.contrib import admin
from .models import Teacher, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','teacher',)
    list_filter = ('teacher',)
    search_fields = ('name', 'teacher',)  # Filter by teacher's name

