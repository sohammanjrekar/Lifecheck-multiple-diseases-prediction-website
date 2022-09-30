from django.shortcuts import render
from .models import Patients, Contact
from django import forms
from django.conf.urls.static import static
import pandas as pd
import pickle
# Create your views here.
def index(request):
    return render(request ,'backend/index.html')

def about(request):
    return render(request ,'backend/about.html')

def blog(request):
    return render(request ,'backend/blog.html') 

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'backend/contact.html', {'thank': thank})
    
def diabetes(request):
    return render(request ,'backend/diseases/diabetes.html')

def result1(request):
    v1 = request.GET['v1']
    v2 = request.GET['v2']
    v3 = request.GET['v3']
    v4 = request.GET['v4']
    v5 = request.GET['v5']
    v6 = request.GET['v6']
    v7 = request.GET['v7']
    v8 = request.GET['v8']
    model = pickle.load(open('lifecheck/backend/static/backend/models/diabetes','rb'))
    result = model.predict([['v1','v2','v3','v4','v5','v6','v7','v8']])
    print(result)
    ans=""
    if(result == [1]):
        ans = "Positive"
    
    else:ans  = "Negative"
    return render(request, 'backend/diseases/diabetes.html', {'result':ans})


def parkinsons(request):
    return render(request ,'backend/diseases/parkinsons.html')

def heart(request):
    return render(request ,'backend/diseases/heart.html')


