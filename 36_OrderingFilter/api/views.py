from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.models import Student
from api.serializers import StudentSerializer
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# *admin ID & PWD - (superuser, superuser)
# *user1, user2 - (pwd - user@12345)

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (OrderingFilter,)
    # ordering_fields = ('name',)
    ordering_fields = ('name', 'city')