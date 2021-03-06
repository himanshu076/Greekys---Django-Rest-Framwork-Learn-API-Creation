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
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]



# Method

# Token generated using username & password
# first install pip install httpie
# CMD - http POST http://127.0.0.1:8000/gettoken/ username="user" password="user_001"


# Token Generated By,
# 1. Using Admin Application
# 2. Using django manage.py commond - python manage.py drf_create_token <user>
# 3. by exposing an API endpoint
# 4. Using Signals