from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.

# Model Object - Single student data

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data)

# Query set - All student data
def student_list(request):
    stu = Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu, many=True)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)