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
        name = request.POST.POST('name', '')
        email = request.POST.POST('email', '')
        phone = request.POST.POST('phone', '')
        desc = request.POST.POST('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'backend/contact.html', {'thank': thank})
    
def diabetes(request):
    return render(request ,'backend/diseases/diabetes.html')

def result_diabetes(request):
    if request.method == 'POST':
        v1 = request.POST['v1']
        v2 = request.POST['v2']
        v3 = request.POST['v3']
        v4 = request.POST['v4']
        v5 = request.POST['v5']
        v6 = request.POST['v6']
        v7 = request.POST['v7']
        v8 = request.POST['v8']
        
        v1 = float(v1)
        v2 =float(v2)
        v3 = float(v3)
        v4 = float(v4)
        v5 = float(v5)
        v6 = float(v6)
        v7 = float(v7)
        v8 = float(v8)
        
        # model = pickle.load(open('lifecheck/backend/static/backend/models/diabetes','rb'))
        with open('C:\\Users\\mrsoh\\Desktop\\Lifecheck-multiple-diseases-prediction-website\\models\diabetes', 'rb') as f:
            model = pickle.load(f)
            result = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8]])
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


