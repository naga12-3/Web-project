from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request,'login.html') 
    
def donation(request):
    return render(request,'donation.html')

def home(request):
    return render(request,'home.html') 
def profile(request):
    return render(request,'profile.html') 
