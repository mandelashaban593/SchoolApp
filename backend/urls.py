from django.contrib import admin
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('api/teachers/', TeacherList.as_view(), name='teacher-list'),
    #path('api/teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    path('api/students', views.students_list, name='student-list'),

     path('api/students/<int:pk>', views.student_get, name='student-detail'),
     path('api/studentUpdate/<int:pk>', views.student_update, name='studentUpdate'),
     path('api/studentDelete/<int:pk>/', views.student_delete, name='studentDelete'),

    #teacher's url
    path('api/teachers', views.teachers_list, name='teacher-list'),
    path('api/teachers/<int:pk>', views.teacher_get, name='teacher-detail'),
    path('api/teacherUpdate/<int:pk>', views.teacher_update, name='teacherUpdate'),
     path('api/teacherDelete/<int:pk>/', views.teacher_delete, name='teacherDelete'),
]

