from django.db import models

# Create your models here.
class Patinet(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
