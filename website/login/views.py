from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Donation


# Create your views here.
name='divya'
def login(request):
    global name
    if request.method=='POST':
        username=request.POST['user_name1']
       
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            name=user.username
            return render(request,'home2.html',{'name':user.username});
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['first_name1']
        lastname=request.POST['last_name1']
        username=request.POST['user_name1']
        email=request.POST['email']
       
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Taken")
            return render(request,'login.html')
        else:

            user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
            user.save()

            return  render(request,'login.html')
    
def donation(request):
    if request.method=='POST':
        donor_name=request.POST['donor_name']
        food_item=request.POST['food_item']
        quantity=request.POST['quantity']
        food_timing=request.POST['food_timing']
        date=request.POST['date'] 
        time=request.POST['time']
        address=request.POST['address']
        

        donor=Donation(donorname=donor_name,fooditem=food_item,quantity=quantity,foodtiming=food_timing,date=date,time=time,address=address)
        donor.save()

        return  render(request,'home2.html',{'name':name})
    else:
        return render(request,'donation.html')

def home(request):
    return render(request,'home.html') 

def home2(request):
    global name
    return render(request,'home2.html',{'name':name})
def profile(request):
    count=0
    users=request.user
    
    donations=Donation.objects.filter(donorname=users.username)

    
    if donations is not None:
        count=len(donations)
    else:
        count=0
        

    context={
        'user': request.user,
        'donations':count
    }
    return render(request,'profile.html',context) 

def diet(request):
    return render(request,'diet.html')

def diet2(request):
    return render(request,'diet2.html',{'name':name})


