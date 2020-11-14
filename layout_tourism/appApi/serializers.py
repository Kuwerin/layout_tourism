from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property
        fields = ('id','owner','name', 'address', 'space', 'cadastral_number', 'state_description', 'state_description', 'contact_person', 'phone_number', 'img_url1', 'img_url2', 'img_url3', 'img_url4', 'img_url5')
