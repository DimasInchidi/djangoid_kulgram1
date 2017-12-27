"""kulgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path

from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token, obtain_jwt_token
from portofool_io.views import RegisterAPIView, UserProfilesAPIView, SingleUserProfileAPIView
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('auth/', obtain_jwt_token, name='token_get'),
    path('auth/verify/', verify_jwt_token, name='token_verify'),
    path('auth/refresh/', refresh_jwt_token, name='token_refresh'),
    path('register/', RegisterAPIView.as_view()),
    path('profiles/', UserProfilesAPIView.as_view()),
    path('my-profile/', SingleUserProfileAPIView.as_view()),
]

if settings.DEBUG:
    schema_view = get_swagger_view(title='Kulgram API')
    urlpatterns.append(
        path('', schema_view),
    )
