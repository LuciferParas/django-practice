import email
from email.mime import image
from email.policy import default
from msilib.schema import ServiceControl
from django.db import models
from pandas import notnull

# Create your models here.

class detailsdata(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    contact = models.IntegerField()
    address = models.CharField(default="address",max_length=90)
    services = models.CharField(default="services",max_length=90)