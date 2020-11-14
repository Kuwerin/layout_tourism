from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Property(models.Model):
    owner = models.CharField(max_length=300, default=None, null=True)
    name = models.CharField(max_length=300, default=None, null=True)
    address = models.CharField(max_length=300, default=None, null=True)
    space = models.FloatField(default=None, null=True)
    cadastral_number = models.CharField(max_length=150, default=None)
    state_description = models.TextField()
    contact_person = models.CharField(max_length=100, default=None)
    phone_number = models.CharField(max_length=12, blank=True)
    img_url1 = models.URLField(blank=True)
    img_url2 = models.URLField(blank=True)
    img_url3 = models.URLField(blank=True)
    img_url4 = models.URLField(blank=True)
    img_url5 = models.URLField(blank=True)
    pretenders_list = ArrayField(models.IntegerField(blank=True, null=True), blank=True, null=True, default=list) 
    updated = models.DateTimeField(auto_now=True, blank=True)
