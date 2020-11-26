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
           # name=user.username
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
        users=request.user
        name=users.username
        #phone='9908248099'
        #address='add'
        #building='sudha'
        if(c_i_t_y=='Tirupati'):
            phone='6303435585, 9100224011'
            address='Shanath nagar, Beside central Park, Mille brown Road, Tirupati-517619'
            building='2-38/B , Vasavi Villa'
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
        elif(c_i_t_y=='Vizag'):
            phone='9381861337, 9100224011'
            address='Venugoap nagar, Beside ZP High School, Tilak Road, Vizag-531022'
            building='3-345/A , Nagadevi Nivas, '
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})

        elif(c_i_t_y=='Bhimavaram'):
            phone='9908248099, 9100224011'
            address='Ravi Puram, Near MAX showroom, JN Road, Bhimavaram-534201'
            building='6-67/c , Sai Apartments '
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
        elif(c_i_t_y=='Rajahmundry'):
            phone='9381861337, 9553665585'
            address='Rajnagar, Beside SBI main branch, Danavaipeta , Rajahmundry-533105'
            building='3-36/a/23 , Chandrika Manikya '
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
        elif(c_i_t_y=='Vijayawada'):
            phone='6303435585, 9553665585'
            address='PV Circle, Beside IMAX, Tilak Road, Vijayawada-520001'
            building='5-55/6 , Royal Town'
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
            #return  redirect('thankyou')
        return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
    else:
        users=request.user
        name1=users.first_name+""+users.last_name
        name=users.username
        print(name1)
        return render(request,'donation.html',{'name':name,'name1':name1})

def home(request):
    donations=Donation.objects.count()
    count1=User.objects.count()
    count=donations
    print(count1,count)
    count2=int(count*1.5)
    return render(request,'home.html',{'count1':count1,'count':count,'count2':count2}) 

def home2(request):
    donations=Donation.objects.count()
    count1=User.objects.count()
    count=donations
    
    print(count1,count)
    users=request.user
    name=users.username
    count2=int(count*1.5)
    return render(request,'home2.html',{'name':name,'count1':count1,'count':count,'count2':count2})
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
    count1=count
    points=0
    Donor='No'
    if(count==0):
        points=0
        count=True
    else:
        points=count*5+int(count/10)*10
        count=False
        Donor='Yes'
    context={
        'user': request.user,
        'donations':count1,
        'volunteer': 'No',
        'phone':phone,
        'donation':d,
        'count'  : count,
        'points':points,
        'Donor':Donor

    }
    return render(request,'profile.html',context) 

def diet(request):
    return render(request,'diet.html')

def diet2(request):
    users=request.user
    name=users.username
    return render(request,'diet2.html',{'name':name})

def pdiet(request):
    if request.method=='POST':
        l1=request.POST.getlist('loki')
        l=[False for i in range(10)]
        for i in l1:
            l[int(i)-1]=True

        obj=[]
        p11=['Eating certain foods while limiting others can help people with diabetes manage their blood sugar levels.',
        'A diet rich in vegetables, fruits, and healthful proteins can have significant benefits for people with diabetes.',
        'Balancing certain foods can help maintain health, improve overall well-being, and prevent future complications.']
        p12=['FattyFish','Leafy Vegetables','Avacados','Eggs','Chia seeds','Beans','Nuts','Greek Yogurt','Almonds','Cashews','Walnuts','Broculi','strawberries','garlic']
        p21=['''Fiddling with diet to control cholesterol makes perfect sense. After all, some of the cholesterol that ends up in arteries starts out in food. Changing your diet to control blood pressure doesn't seem quite so straightforward. Yet food can have a direct and sometimes dramatic effect on blood pressure.''',
            '''Salt certainly plays a role. But there is far more to a blood pressure–friendly diet than minimizing salt intake. Fruits, vegetables, low-fat dairy foods, beans, nuts, whole-grain carbohydrates, and unsaturated fats also have healthful effects on blood pressure. ''']
        p22=['Citrus fruits', 'Salmon and other fatty fish', 'Swiss chard', 'Pumpkin seeds', 'Beans and lentils', 'Berries', 'Amarnath', 'Pistachios', 'Carrots', 'Celery', 'Tomatoes and tomato products', 'Broccoli', 'Greek yogurt', 'Herbs and spices']
        p31=['''Diet is an extremely important part of the daily lifestyle choices you make. Foods you eat and the dietary supplements you take affect your overall health as well as the health of your eyes.''','''A diet high in saturated fat and sugar may increase your risk of eye disease. On the other hand, healthy foods such as greens and fruits may help prevent certain eye diseases and other health problems.''','''The best foods for getting your daily dose of vitamin C are fruits and vegetables, including oranges, grapefruit, strawberries and broccoli. Vitamin E. If you already have AMD, make sure to get enough vitamin E. Studies have shown that this vitamin plays a role in slowing down the disease.''']
        p32=['tuna', 'salmon', 'trout', 'mackerel', 'sardines', 'walnuts', 'Brazil nuts', 'cashews', 'peanuts', 'lentils', 'chia seeds', 
        'flax seeds', 'hemp seeds', 'lemons', 'oranges', 'grapefruits', ' Leafy green vegetables', ' Carrots', ' Sweet potatoes', ' Beef', ' Eggs']
        p41=['''As of now, no cure for glaucoma exists and the drugs used to treat it are primarily focused on lowering the elevated eye pressure. However, this doesn’t always succeed in preventing the further progression of the condition.''',
        '''Diet regulation can also serve as one of the best ways to stay away from this disease, according to a host of research studies, helping to naturally relieve IOP (intraocular pressure), improving blood flow to the eye and reducing oxidative stress.''','Certain fruits and vegetables with higher vitamin A and C content have been shown to reduce glaucoma risk as well.' ] 
        p42=['collard greens', 'cabbage', 'kale', 'spinach', 'Brussels', 'sprouts', 'celery', 'carrots', 'peaches', 'radishes', 'green beans', 
        'beets', 'oranges', 'Blackcurrants', 'Goji Berries', 'Eggplant', 'Sea food', 'Drink GreenTea'] 
        p51=['''There’s no special asthma diet. We don’t know of any foods that reduce the airway inflammation of asthma. Beverages that contain caffeine provide a slight amount of bronchodilation for an hour or two, but taking a rescue inhaler is much more effective for the temporary relief of asthma symptoms.''',
        '''However, a good diet is an important part of your overall asthma treatment plan. Just like regular exercise, a healthy diet is good for everyone. That goes for people with asthma, too. Obesity is associated with more severe asthma, so you want to take steps to maintain a healthy weight.''','Vitamin D rich foods, such as milk and eggs', 'Beta carotene-rich vegetables, such as carrots and leafy greens', 
        'Magnesium rich food, such as spinach and pumpkin seeds']
        p52=['Salmon', 'Milk and fortified milk', 'Eggs', 'Fortified orange juice', 'Carrots', 'Sweet potatoes', 'Broccoli', 'Apple ', 
        'Banana', 'Dark chocolate', 'Spinach ', 'Pumpkin seeds', 'Swiss chard']
        p61=['Look for a wide array of proteins','While having some fats in your diet is healthy, it\'s important not to go overboard. In particular, try to avoid saturated and trans fats.'
        , 'Most people with hepatitis C will not have to follow a special diet unless their liver is badly damaged. However, a healthful diet can help manage hepatitis C and prevent complications and related conditions from developing.']
        p62=['poultry', 'fish', 'beans', 'nuts', 'seeds', 'milk', 'yogurt ', 'cheese', 'Plenty of fruits and vegetables.', ' oats', 
        ' brown rice', ' barley', ' quinoa', ' skinless chicken', ' egg whites', 'Low-fat or non-fat dairy products', ' avocados', ' olive oil']
        p71=['''Although you might know that eating certain foods can increase your heart disease risk, it's often tough to change your 
        eating habits. Whether you have years of unhealthy eating under your belt or you simply want to fine-tune your diet. ''',
        '''Once you know which foods to eat more of and which foods to limit, you'll be on your way toward a heart-healthy diet.''']
        p72=['Leafy Green Vegetables', 'Whole Grains', 'Berries', 'Avocados', 'Fatty Fish and Fish Oil', 'Walnuts', 'Beans', 'Dark Chocolate', 'Tomatoes',
                'Almonds', 'Seeds', 'Garlic', 'Olive oil', 'Green tea']
        p81=['''It is often better that a person with TB has the same diet as normal but possibly with some changes being made to increase their intake of food. People with TB often have a poor appetite initially,
         but having more frequent food intake can be helpful.''','''Within a few weeks of starting TB treatment, the person’s appetite should increase and come back to normal.
          A person with TB should aim to have three meals and three snacks each day to increase the amount of food they eat''']
        p82=[' banana', ' cereal porridge', ' peanut chikki', ' wheat ', ' ragi', ' orange', ' mango', ' sweet pumpkin ', ' carrots', ' guava', 
        'amla', 'tomato', ' nuts ', ' seeds ']
        p91=['''Food plays an important role in treating a lot of diseases, it is highly advised to eat a balanced diet, which contains all kinds of nutrients to ensure a healthy system. Alzheimer’s is a complicated disease in which the patient starts losing memory and concentration.''',
        '''Alzheimer’s disease needs proper medical attention and treatment to get cured. With the medical aid, patients are advised to have a proper diet, which contains a lot of brain-boosting foods. These food items contain certain nutrients that might help in delaying the symptoms of this disease and improve the quality of life.''']
        p92=['Berries', 'Nuts', 'Omega-3s', 'Cruciferous Vegetables', 'Spices', 'Seeds', 'Leafy vegetables', ' low-fat dairy', ' olive oil', 
        'Broccoli', 'cauliflower ', 'brussels sprouts', 'Avacados', 'pumpkin seeds', 'poultry']
                  

        obj.append(data([],"Diabetes",l[0],p11,p12,[]))
        obj.append(data([],"Blood Pressure",l[1],p21,p22,[]))
        obj.append(data([],"Presbyopia",l[2],p31,p32,[]))
        obj.append(data([],"Glaucoma",l[3],p41,p42,[]))
        obj.append(data([],"Asthma",l[4],p51,p52,[]))
        obj.append(data([],"Hepatitis",l[5],p61,p62,[]))
        obj.append(data([],"Cardio",l[6],p71,p72,[]))
        obj.append(data([],"Tuberculosis",l[7],p81,p82,[]))
        obj.append(data([],"Dementia and Alzheimers",l[8],p91,p92,[]))
        
        
        for i in range(9):
            print(obj[i].im,obj[i].desc,obj[i].val)

    
        return render(request,'age1.html',{'obj':obj})
def pdiet2(request):
    if request.method=='POST':
        l1=request.POST.getlist('loki')
        l=[False for i in range(10)]
        for i in l1:
            l[int(i)-1]=True

        obj=[]
        p11=['Eating certain foods while limiting others can help people with diabetes manage their blood sugar levels.',
        'A diet rich in vegetables, fruits, and healthful proteins can have significant benefits for people with diabetes.',
        'Balancing certain foods can help maintain health, improve overall well-being, and prevent future complications.']
        p12=['FattyFish','Leafy Vegetables','Avacados','Eggs','Chia seeds','Beans','Nuts','Greek Yogurt','Almonds','Cashews','Walnuts','Broculi','strawberries','garlic']
        p21=['''Fiddling with diet to control cholesterol makes perfect sense. After all, some of the cholesterol that ends up in arteries starts out in food. Changing your diet to control blood pressure doesn't seem quite so straightforward. Yet food can have a direct and sometimes dramatic effect on blood pressure.''',
            '''Salt certainly plays a role. But there is far more to a blood pressure–friendly diet than minimizing salt intake. Fruits, vegetables, low-fat dairy foods, beans, nuts, whole-grain carbohydrates, and unsaturated fats also have healthful effects on blood pressure. ''']
        p22=['Citrus fruits', 'Salmon and other fatty fish', 'Swiss chard', 'Pumpkin seeds', 'Beans and lentils', 'Berries', 'Amarnath', 'Pistachios', 'Carrots', 'Celery', 'Tomatoes and tomato products', 'Broccoli', 'Greek yogurt', 'Herbs and spices']
        p31=['''Diet is an extremely important part of the daily lifestyle choices you make. Foods you eat and the dietary supplements you take affect your overall health as well as the health of your eyes.''','''A diet high in saturated fat and sugar may increase your risk of eye disease. On the other hand, healthy foods such as greens and fruits may help prevent certain eye diseases and other health problems.''','''The best foods for getting your daily dose of vitamin C are fruits and vegetables, including oranges, grapefruit, strawberries and broccoli. Vitamin E. If you already have AMD, make sure to get enough vitamin E. Studies have shown that this vitamin plays a role in slowing down the disease.''']
        p32=['tuna', 'salmon', 'trout', 'mackerel', 'sardines', 'walnuts', 'Brazil nuts', 'cashews', 'peanuts', 'lentils', 'chia seeds', 
        'flax seeds', 'hemp seeds', 'lemons', 'oranges', 'grapefruits', ' Leafy green vegetables', ' Carrots', ' Sweet potatoes', ' Beef', ' Eggs']
        p41=['''As of now, no cure for glaucoma exists and the drugs used to treat it are primarily focused on lowering the elevated eye pressure. However, this doesn’t always succeed in preventing the further progression of the condition.''',
        '''Diet regulation can also serve as one of the best ways to stay away from this disease, according to a host of research studies, helping to naturally relieve IOP (intraocular pressure), improving blood flow to the eye and reducing oxidative stress.''','Certain fruits and vegetables with higher vitamin A and C content have been shown to reduce glaucoma risk as well.' ] 
        p42=['collard greens', 'cabbage', 'kale', 'spinach', 'Brussels', 'sprouts', 'celery', 'carrots', 'peaches', 'radishes', 'green beans', 
        'beets', 'oranges', 'Blackcurrants', 'Goji Berries', 'Eggplant', 'Sea food', 'Drink GreenTea'] 
        p51=['''There’s no special asthma diet. We don’t know of any foods that reduce the airway inflammation of asthma. Beverages that contain caffeine provide a slight amount of bronchodilation for an hour or two, but taking a rescue inhaler is much more effective for the temporary relief of asthma symptoms.''',
        '''However, a good diet is an important part of your overall asthma treatment plan. Just like regular exercise, a healthy diet is good for everyone. That goes for people with asthma, too. Obesity is associated with more severe asthma, so you want to take steps to maintain a healthy weight.''','Vitamin D rich foods, such as milk and eggs', 'Beta carotene-rich vegetables, such as carrots and leafy greens', 
        'Magnesium rich food, such as spinach and pumpkin seeds']
        p52=['Salmon', 'Milk and fortified milk', 'Eggs', 'Fortified orange juice', 'Carrots', 'Sweet potatoes', 'Broccoli', 'Apple ', 
        'Banana', 'Dark chocolate', 'Spinach ', 'Pumpkin seeds', 'Swiss chard']
        p61=['Look for a wide array of proteins','While having some fats in your diet is healthy, it\'s important not to go overboard. In particular, try to avoid saturated and trans fats.'
        , 'Most people with hepatitis C will not have to follow a special diet unless their liver is badly damaged. However, a healthful diet can help manage hepatitis C and prevent complications and related conditions from developing.']
        p62=['poultry', 'fish', 'beans', 'nuts', 'seeds', 'milk', 'yogurt ', 'cheese', 'Plenty of fruits and vegetables.', ' oats', 
        ' brown rice', ' barley', ' quinoa', ' skinless chicken', ' egg whites', 'Low-fat or non-fat dairy products', ' avocados', ' olive oil']
        p71=['''Although you might know that eating certain foods can increase your heart disease risk, it's often tough to change your 
        eating habits. Whether you have years of unhealthy eating under your belt or you simply want to fine-tune your diet. ''',
        '''Once you know which foods to eat more of and which foods to limit, you'll be on your way toward a heart-healthy diet.''']
        p72=['Leafy Green Vegetables', 'Whole Grains', 'Berries', 'Avocados', 'Fatty Fish and Fish Oil', 'Walnuts', 'Beans', 'Dark Chocolate', 'Tomatoes',
                'Almonds', 'Seeds', 'Garlic', 'Olive oil', 'Green tea']
        p81=['''It is often better that a person with TB has the same diet as normal but possibly with some changes being made to increase their intake of food. People with TB often have a poor appetite initially,
         but having more frequent food intake can be helpful.''','''Within a few weeks of starting TB treatment, the person’s appetite should increase and come back to normal.
          A person with TB should aim to have three meals and three snacks each day to increase the amount of food they eat''']
        p82=[' banana', ' cereal porridge', ' peanut chikki', ' wheat ', ' ragi', ' orange', ' mango', ' sweet pumpkin ', ' carrots', ' guava', 
        'amla', 'tomato', ' nuts ', ' seeds ']
        p91=['''Food plays an important role in treating a lot of diseases, it is highly advised to eat a balanced diet, which contains all kinds of nutrients to ensure a healthy system. Alzheimer’s is a complicated disease in which the patient starts losing memory and concentration.''',
        '''Alzheimer’s disease needs proper medical attention and treatment to get cured. With the medical aid, patients are advised to have a proper diet, which contains a lot of brain-boosting foods. These food items contain certain nutrients that might help in delaying the symptoms of this disease and improve the quality of life.''']
        p92=['Berries', 'Nuts', 'Omega-3s', 'Cruciferous Vegetables', 'Spices', 'Seeds', 'Leafy vegetables', ' low-fat dairy', ' olive oil', 
        'Broccoli', 'cauliflower ', 'brussels sprouts', 'Avacados', 'pumpkin seeds', 'poultry']
                  

        obj.append(data([],"Diabetes",l[0],p11,p12,[]))
        obj.append(data([],"Blood Pressure",l[1],p21,p22,[]))
        obj.append(data([],"Presbyopia",l[2],p31,p32,[]))
        obj.append(data([],"Glaucoma",l[3],p41,p42,[]))
        obj.append(data([],"Asthma",l[4],p51,p52,[]))
        obj.append(data([],"Hepatitis",l[5],p61,p62,[]))
        obj.append(data([],"Cardio",l[6],p71,p72,[]))
        obj.append(data([],"Tuberculosis",l[7],p81,p82,[]))
        obj.append(data([],"Dementia and Alzheimers",l[8],p91,p92,[]))
        
        
        for i in range(9):
            print(obj[i].im,obj[i].desc,obj[i].val)

        users=request.user
        name=users.username
        return render(request,'age2.html',{'obj':obj,'name':name})

       

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
        c_i_t_y=city
        if(c_i_t_y=='Tirupati'):
            phone='6303435585, 9100224011'
            address='Shanath nagar, Beside central Park, Mille brown Road, Tirupati-517619'
            building='2-38/B , Vasavi Villa'
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
        elif(c_i_t_y=='Vizag'):
            phone='9381861337, 9100224011'
            address='Venugoap nagar, Beside ZP High School, Tilak Road, Vizag-531022'
            building='3-345/A , Nagadevi Nivas, '
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})

        elif(c_i_t_y=='Bhimavaram'):
            phone='9908248099, 9100224011'
            address='Ravi Puram, Near MAX showroom, JN Road, Bhimavaram-534201'
            building='6-67/c , Sai Apartments '
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
        elif(c_i_t_y=='Rajahmundry'):
            phone='9381861337, 9553665585'
            address='Rajnagar, Beside SBI main branch, Danavaipeta , Rajahmundry-533105'
            building='3-36/a/23 , Chandrika Manikya '
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
        elif(c_i_t_y=='Vijayawada'):
            phone='6303435585, 9553665585'
            address='PV Circle, Beside IMAX, Tilak Road, Vijayawada-520001'
            building='5-55/6 , Royal Town'
            #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})
        
        donations=Donation.objects.filter(city=city, date=x)
        if(len(donations)==0):
            val=True
        #print(donations,donations[0].date)
        #if(x==str(donations[0].date)):
            #print('Dates are equal')
        val1=not val
        users=request.user
        name=users.username

        return render(request,'volunteer.html',{'donation':donations,'val':val,'place':city,'val1':val1,'date':x,'name':name,'phone':phone,'address':address,'building':building})
    users=request.user
    name=users.username
    return render(request,'volunteer.html',{'donation':donations,'val':val,'place':'','name':name})


def map(request):
    a= [{ 'lat': 13.035246, 'lng': 77.553655 },{ 'lat': +17.4169, 'lng': 78.4387 },{ 'lat': 17.4239, 'lng': 78.4738 }];
    dataJSON = dumps(a) 
    return render(request, 'map.html', {'a': dataJSON})

def thankyou(request):
    global c_i_t_y
    users=request.user
    name=users.username
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
        phone='6303435585, 9553665585'
        address='PV Circle, Beside IMAX, Tilak Road, Vijayawada-520001'
        building='5-55/6 , Royal Town'
        return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building})

    #return render(request,'thankyou.html',{'name':name,'phone':phone,'address':address,'building':building});

def money(request):
    users=request.user
    name=users.username
    return render(request,'Money.html',{'name':name})

def aboutus(request):
    return render(request,'Aboutus.html')

def aboutus2(request):
    users=request.user
    name=users.username
    return render(request,'Aboutus2.html',{'name':name})


def knowmore1(request):
    return render(request,'knowmore1.html')
def knowmore2(request):
    return render(request,'knowmore2.html')

def knowmore3(request):
    return render(request,'knowmore3.html')

def knowmore12(request):
    users=request.user
    name=users.username
    return render(request,'knowmore12.html',{'name':name})

def knowmore22(request):
    users=request.user
    name=users.username
    return render(request,'knowmore22.html',{'name':name})

def knowmore32(request):
    users=request.user
    name=users.username
    return render(request,'knowmore32.html',{'name':name})

