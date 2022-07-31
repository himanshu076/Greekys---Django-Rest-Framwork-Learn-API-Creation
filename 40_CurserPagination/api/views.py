from django.shortcuts import render
from api.serializers import StudentSerializer
from api.models import Student
from rest_framework.generics import ListAPIView
from api.my_pagination import MyCursorPagination

# ID & PWD - (superuser, superuser)

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination