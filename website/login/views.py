from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Donation
from .models import data
import datetime
from django.shortcuts import render 
from json import dumps 
  
  
def maps(request): 
    # create data dictionary 
    dataDictionary =[{ 'lat': 13.035246, 'lng': 77.553655 }]
    # dump data 
    dataJSON = dumps(dataDictionary) 
    return render(request, 'maps.html', {'data': dataJSON}) 


# Create your views here.
name='User'
c_i_t_y='None'
def login(request):
    global name
    if request.method=='POST':
        username=request.POST['user_name1']
       
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        val=False
        if user is not None:
            auth.login(request,user)
            name=user.username
            #return render(request,'home2.html',{'name':user.username});
            return redirect('home2')
        else:
            val=True
            messages.info(request,"Invalid Credentials")
            invalid='Invalid Credentials'
            return render(request,'login.html',{'msg':invalid})
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

        global c_i_t_y
        c_i_t_y=city
        return  redirect('thankyou')
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


def volunteer(request):
    donations=[]
    val=False
    if request.method=='POST':
        city='none'
        try:
            city=request.POST['city']
        except:
            print(city,'hi rohit')

        x = str(datetime.datetime.now()).split()[0]
        
        
        donations=Donation.objects.filter(city=city, date=x)
        if(len(donations)==0):
            val=True
        #print(donations,donations[0].date)
        #if(x==str(donations[0].date)):
            #print('Dates are equal')
        val1=not val
        return render(request,'volunteer.html',{'donation':donations,'val':val,'place':city,'val1':val1,'date':x})

    return render(request,'volunteer.html',{'donation':donations,'val':val,'place':''})


def map(request):
    a= [{ 'lat': 13.035246, 'lng': 77.553655 },{ 'lat': +17.4169, 'lng': 78.4387 },{ 'lat': 17.4239, 'lng': 78.4738 }];
    dataJSON = dumps(a) 
    return render(request, 'map.html', {'a': dataJSON})

def thankyou(request):
    global name,c_i_t_y
    #phone='9908248099'
    #address='add'
    #building='sudha'
    if(c_i_t_y=='Tirupati'):
        phone='6303435585, 9100224011'
        address='Shanath nagar, Beside central Park, Mille brown Road, Tirupati-517619'
        building='2-38/B , Vasavi Villa'
        return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
    elif(c_i_t_y=='Vizag'):
        phone='9381861337, 9100224011'
        address='Venugoap nagar, Beside ZP High School, Tilak Road, Vizag-531022'
        building='3-345/A , Nagadevi Nivas, '
        return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})

    elif(c_i_t_y=='Bhimavaram'):
        phone='9908248099, 9100224011'
        address='Ravi Puram, Near MAX showroom, JN Road, Bhimavaram-534201'
        building='6-67/c , Sai Apartments '
        return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
    elif(c_i_t_y=='Rajahmundry'):
        phone='9381861337, 9553665585'
        address='Rajnagar, Beside SBI main branch, Danavaipeta , Rajahmundry-533105'
        building='3-36/a/23 , Chandrika Manikya '
        return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
    elif(c_i_t_y=='Vijayawada'):
        phone='7382906527, 9553665585'
        address='PV Circle, Beside IMAX, Tilak Road, Vijayawada-520001'
        building='5-55/6 , Royal Town'
        return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})

    #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building});
