import email
from django.db import models

# Create your models here.

class detailsdata(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    contact = models.IntegerField()