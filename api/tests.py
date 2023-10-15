# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student, Teacher
from .serializers import StudentSerializer
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .views import student_get,teacher_get,teacher_update,teachers_list,students_list,student_update

class StudentTeacherListTests(APITestCase):
    def setUp(self):
        # Create a teacher for the foreign key reference
        self.teacher = Teacher.objects.create(name='John Doe')
        self.teacher_data = {'name': self.teacher.name}
        self.student_data = Student.objects.create(name='Alice', surname='Smith', teacher=self.teacher)
        self.factory = APIRequestFactory()

    def test_get_students(self):
        # Create a sample student with a foreign key reference
        student = Student.objects.create(name='Alice', teacher=self.teacher)

        url = reverse('student-list')  # Replace 'students-list' with the actual URL name
        response =response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if one student is returned


    def test_get_teachers(self):
        # Create a sample student with a foreign key reference
        teacher = Teacher.objects.create(name='Masha Monk')

        url = reverse('teacher-list')  # Replace 'students-list' with the actual URL name
        response =response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if one student is returned


    def test_get_single_teacher(self):
        url = reverse('teacher-detail', args=[self.teacher.id])
        request = self.factory.get(url)
        response = teacher_get(request, pk=self.teacher.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.teacher.name)
       # self.assertEqual(response.data['surname'], self.student.surname)

    def test_update_teacher(self):
        url = reverse('teacherUpdate', args=[self.teacher.id])
        updated_data = {'name': 'Jane'}  # Adjust the data as needed
        request = self.factory.put(url, updated_data, format='json')
        response = teacher_update(request, pk=self.teacher.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])



    def test_create_teacher(self):
        url = reverse('teacher-list')  # Adjust the URL name as needed
        request = self.factory.post(url, self.teacher_data, format='json')
        response = teachers_list(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_create_student(self):
    #     url = reverse('student-list')  # Adjust the URL name as needed
    #     student = {'name':'Alice','surname':'Mary', 'teacher':self.teacher}
    #     request = self.client.post(url, student, format='json')
    #     response = students_list(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)