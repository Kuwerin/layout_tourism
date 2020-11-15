from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
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
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)


class SearchUserByNameView(APIView):
    def get(self, request):
        user_name = request.GET.get('username', '')
        users = User.objects.filter(username=user_name)
        serializer = UserSerializer(users, many=True)
        return Response({'users':serializer.data})
