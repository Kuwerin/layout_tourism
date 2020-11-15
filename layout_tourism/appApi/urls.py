"""layout_tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('property', PropertyViewSet, basename='property-api')
router.register('user', UserViewSet, 'user-api')

urlpatterns = router.urls
urls = [
        path('search/', SearchUserByNameView.as_view()),
        path('apitoken/', views.obtain_auth_token)
        ]
[urlpatterns.append(url) for url in urls]
# urlpatterns = [
#     path('', index),
# ]
