from typing import List
from django.contrib import admin
from api01.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'roll', 'city']
