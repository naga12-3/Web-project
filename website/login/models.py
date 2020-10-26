from django.db import models

# Create your models here.

class Donation(models.Model):
    donorname=models.CharField(max_length=100)
    fooditem=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    foodtiming=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    address=models.TextField()
