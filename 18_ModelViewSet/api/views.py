from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers, viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer