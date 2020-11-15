from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('property', PropertyViewSet, basename='property-api')
router.register('user', UserViewSet, 'user-api')

urlpatterns = router.urls
urls = [
        path('search/', SearchUserByNameView.as_view()),
        path('token/', TokenObtainPairView.as_view()),
        path('token/refresh/', TokenRefreshView.as_view())
        ]
[urlpatterns.append(url) for url in urls]
