from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),

]




# Command -

# Initial login & Get Token
    # http POST http://127.0.0.1:8000/gettoken/ username="user" password="user_001"

# Refresh Token
    # http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzOTE0MTU1NCwiaWF0IjoxNjM5MDU1MTU0LCJqdGkiOiI4ODA0MzkwYmI1ZjQ0YTY1YTk0MjJmZWMyOTFkNzBmZSIsInVzZXJfaWQiOjJ9.j8Ca_amNWJJwm69-plPMv7VChzRwPcwJITlhpEq4M-c"

# Verify Token
    # http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MDU2Mzk4LCJpYXQiOjE2MzkwNTUxNTQsImp0aSI6ImQzYzY0MTA1MDA5NDRiOGY4YmYwNzNiMjAwMTA4NmE5IiwidXNlcl9pZCI6Mn0.3MzO5eUvG__cszlBvHKaPRfX_t2nD5f4-MM4OyuLI7w"


# ******************************************************************************************

# Authenticatio Through "JWT Token"
# GET Request JWT Token
    # http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MTE1MDM2LCJpYXQiOjE2MzkxMTQxMDMsImp0aSI6ImJlNzIyNWNmMTUwNDQ0M2JiMTU4ODVjZGU2Njc5ZmU1IiwidXNlcl9pZCI6Mn0.VdrUQL1eZ3YTqpgCMwwP-tBz_0koA3-8-wLQEonw9Ms'

# POST Request "JWT Token"
    # http -f POST http://127.0.0.1:8000/studentapi/ name=Raj roll=103 city=Bokaro 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MTE1NjI1LCJpYXQiOjE2MzkxMTQxMDMsImp0aSI6IjQxMzYyMWVlMWNlNjQxMzU5ODMwNWViMzg5NDg1MmVmIiwidXNlcl9pZCI6Mn0.QKrMrmtLNN1u5xaXS3pzCsC1zL2fxhBN6T3bB3O1e30'

# PUT Request "JWT Token"
    # http PUT http://127.0.0.1:8000/studentapi/3/ name=Sonu roll=104 city=Dhaka 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MTE2Mjc3LCJpYXQiOjE2MzkxMTQxMDMsImp0aSI6Ijg5MmIyYTQ1YzEzYjQ1NTFhZGQ2OGQ0MDA3MmJhMzZhIiwidXNlcl9pZCI6Mn0.cKiCP3qRhN8QrXGPde1BXfbwKRG3Vuan9JX633EYavk'

