from django.db import models

# Create your models here.

class Donation(models.Model):
    donorname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    fooditem=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    foodtiming=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address=models.TextField()
    def __str__(self):
        return self.donorname

#class volunteer(models.Model):



class Userregister(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class data:
    im: list
    desc: str
    val: bool
    dis_points:list
    dis_par1:list
    dis_par2:list
    def __init__(self,im,desc,val,dis_points,dis_par1,dis_par2):
        self.im=im
        self.desc=desc
        self.val=val
        self.dis_points=dis_points
        self.dis_par1=dis_par1
        self.dis_par2=dis_par2
    
