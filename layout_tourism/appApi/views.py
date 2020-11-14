from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

def index(request):
    return JsonResponse({'Response':'In API'})


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
