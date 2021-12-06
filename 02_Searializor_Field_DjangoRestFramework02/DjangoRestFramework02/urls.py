from django.contrib import admin
from django.urls import path
from api01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studtcreate/', views.student_create),
]
