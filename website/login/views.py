from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Donation
from .models import data


# Create your views here.
name='User'
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
        phone=request.POST['phone']
        food_item=request.POST['food_item']
        quantity=request.POST['quantity']
        food_timing=request.POST['food_timing']
        date=request.POST['date'] 
        time=request.POST['time']
        city=request.POST['city']
        address=request.POST['address']

        

        donor=Donation(donorname=donor_name,phone=phone,fooditem=food_item,quantity=quantity,foodtiming=food_timing,date=date,time=time,city=city,address=address)
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
    phone='-'
    users=request.user
    
    donations=Donation.objects.filter(donorname=users.username)

    if donations is not None:
        count=len(donations)
        if count>0:
            phone=donations[count-1].phone
    else:
        count=0
        phone='-'
    d=[]
    print(donations)
    j=count
    for i in donations[::-1]:
        d.append([i,j])
        j-=1
    if(count==0):
        count=True
    else:
        count=False
    context={
        'user': request.user,
        'donations':count,
        'volunteer': 'No',
        'phone':phone,
        'donation':d,
        'count'  : count
    }
    return render(request,'profile.html',context) 

def diet(request):
    return render(request,'diet.html')

def diet2(request):
    return render(request,'diet2.html',{'name':name})

def pdiet(request):
    if request.method=='POST':
        age=request.POST['age']
        l1=request.POST.getlist('loki')
        l=[False for i in range(10)]
        for i in l1:
            l[int(i)-1]=True

        obj=[]
        obj.append(data("art1.jpeg","1st disease",l[0]))
        obj.append(data("art2.jpeg","2nd disease",l[1]))
        obj.append(data("art3.jpeg","3rd disease",l[2]))
        obj.append(data("art4.jpeg","4th disease",l[3]))
        obj.append(data("art5.jpeg","5th disease",l[4]))
        obj.append(data("art6.jpeg","6th disease",l[5]))
        obj.append(data("art7.jpeg","7th disease",l[6]))
        obj.append(data("art8.jpeg","8th disease",l[7]))
        obj.append(data("art5.jpeg","9th disease",l[8]))
        obj.append(data("art3.jpeg","10th disease",l[9]))
        for i in range(10):
            print(obj[i].im,obj[i].desc,obj[i].val)

        if(age=='1'):
            return render(request,'age1.html',{'obj':obj})
        elif(age=='2'):
            return render(request,'age2.html')
        elif(age=='3'):
            return render(request,'age3.html')
        elif(age=='4'):
            return render(request,'age4.html')
        elif(age=='5'):
            return render(request,'age5.html')
        return render(request,'home.html')