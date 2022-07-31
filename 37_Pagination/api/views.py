from django.shortcuts import render
from api.serializers import StudentSerializer
from api.models import Student
from rest_framework.generics import ListAPIView

# ID & PWD - (superuser, superuser)

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer