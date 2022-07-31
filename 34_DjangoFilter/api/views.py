from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Student
from api.serializers import StudentSerializer

# *admin ID & PWD - (superuser, superuser)
# *user1, user2 - (pwd - user@12345)

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,)     # locally/ per view django Filter.
    # filterset_fields = ('city',)
    filterset_fields = ('name', 'city',)