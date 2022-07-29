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
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), # This Shown the login button on BrowserAPI Page.
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_view'), # It is used to generate access & refresh token.
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'), # this is used to create access token using refresh token.
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'), # It is used to verify the token is valid or not.
]