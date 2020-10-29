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

class Userregister(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
