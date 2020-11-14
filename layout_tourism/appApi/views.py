from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return JsonResponse({'Response':'In API'})


# class TestView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#                 'user': request.user, # 'django.contrib.auth.User'
#                 'auth': request.auth  # None
#                 }
#         return Response(content)

class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
