from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from rest_framework.authtoken.views import obtain_auth_token
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
    path('gettoken/', obtain_auth_token)
    
]



# Method

# Token generated using username & password
# first install pip install httpie
# CMD - http POST http://127.0.0.1:8000/gettoken/ username="user" password="user_001"