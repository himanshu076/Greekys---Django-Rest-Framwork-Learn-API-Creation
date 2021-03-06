from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
