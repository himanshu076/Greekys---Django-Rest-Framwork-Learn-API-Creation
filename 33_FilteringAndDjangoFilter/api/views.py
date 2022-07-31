from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.models import Student
from api.serializers import StudentSerializer

# *admin ID & PWD - (superuser, superuser)
# user1, user2 - (pwd - user@12345)

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)