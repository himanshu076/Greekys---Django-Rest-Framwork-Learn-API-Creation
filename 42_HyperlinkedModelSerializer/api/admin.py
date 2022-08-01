from django.contrib import admin
from api.models import Student

# Register your models here.
@admin.register(Student)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']