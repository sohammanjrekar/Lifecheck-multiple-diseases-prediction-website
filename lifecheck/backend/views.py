from django.shortcuts import render
from .models import Patient,symptom,disease,Contact
from django import forms
from django.conf.urls.static import static
import pandas as pd
import pickle
import pdfkit
from django.http import HttpResponse
# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 
import sklearn


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
            dia_ans=""
            if(result == [1]):
                dia_ans = "Positive"
            
            else:dia_ans  = "Negative"
            return render(request, 'backend/diseases/diabetes.html', {'result':dia_ans})


def parkinsons(request):
    return render(request ,'backend/diseases/parkinsons.html')


def result_parkinsons(request):
    if request.method == 'POST':
        p1 = float(request.POST['p1'])
        p2 = float(request.POST['p2'])
        p3 = float(request.POST['p3'])
        p4 = float(request.POST['p4'])
        p5 = float(request.POST['p5'])
        p6 =float( request.POST['p6'])
        p7 =float( request.POST['p7'])
        p8 =float( request.POST['p8'])
        p9 = float(request.POST['p9'])
        p10 = float(request.POST['p10'])
        p11 = float(request.POST['p11'])
        p12 = float(request.POST['p12'])
        p13= float(request.POST['p13'])
        p14=float( request.POST['p14'])
        p15=float( request.POST['p15'])
        p16=float( request.POST['p16'])
        p17 = float(request.POST['p17'])
        p18 = float(request.POST['p18'])
        p19 = float(request.POST['p19'])
        p20= float(request.POST['p20'])
        p21= float(request.POST['p21'])
        p22=float( request.POST['p22'])
    
        
        # model = pickle.load(open('lifecheck/backend/static/backend/models/diabetes','rb'))
        with open('C:\\Users\\mrsoh\\Desktop\\Lifecheck-multiple-diseases-prediction-website\\models\parkinsons.sav', 'rb') as f:
            model = pickle.load(f)
            result = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22]])
            print(result)
            park_ans=""
            if(result == [1]):
                park_ans = "Positive"
            
            else:park_ans  = "Negative"
            return render(request, 'backend/diseases/parkinsons.html', {'result':park_ans})









def heart(request):
    return render(request ,'backend/diseases/heart.html')

def result_heart(request):
    if request.method == 'POST':
        h1 = float(request.POST['h1'])
        h2 = float(request.POST['h2'])
        h3 = float(request.POST['h3'])
        h4 = float(request.POST['h4'])
        h5 = float(request.POST['h5'])
        h6 =float( request.POST['h6'])
        h7 =float( request.POST['h7'])
        h8 =float( request.POST['h8'])
        h9 = float(request.POST['h9'])
        h10 = float(request.POST['h10'])
        h11 = float(request.POST['h11'])
        h12 = float(request.POST['h12'])
        h13= float(request.POST['h13'])

    
        
        # model = pickle.load(open('lifecheck/backend/static/backend/models/diabetes','rb'))
        with open('C:\\Users\\mrsoh\\Desktop\\Lifecheck-multiple-diseases-prediction-website\\models\heart.sav', 'rb') as f:

            model = pickle.load(f)
            result = model.predict([[h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13]])
            print(result)
            heart_ans=""
            if(result == [1]):
                heart_ans = "Positive"
            
            else:heart_ans  = "Negative"
            return render(request, 'backend/diseases/heart.html', {'result':heart_ans})
            



# def report(request):
#     return render(request ,'backend/report/report.html')   
  
class diabetes_report(View):
     def get(self, request, *args, **kwargs):
        pdf = html_to_pdf
        ('C:\\Users\\mrsoh\\Desktop\\Lifecheck-multiple-diseases-prediction-website\\lifecheck\\backend\\templates\\backend\\report\\diabetes_report.html')
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
    
    
class heart_report(View):
     def get(self, request, *args, **kwargs):
        pdf = html_to_pdf('C:\\Users\\mrsoh\\Desktop\\Lifecheck-multiple-diseases-prediction-website\\lifecheck\\backend\\templates\\backend\\report\\heart_report.html')
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
    
class parkinsons_report(View):
     def get(self, request, *args, **kwargs):
        pdf = html_to_pdf('C:\\Users\\mrsoh\\Desktop\\Lifecheck-multiple-diseases-prediction-website\\lifecheck\\backend\\templates\\backend\\report\\parkinsons_report.html')
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     pdf = pdfkit.from_file('C:\\Users\\mrsoh\\Desktop\\Lifecheck-multiple-diseases-prediction-website\\lifecheck\\backend\\templates\\backend\\report\\report.html', 'report.pdf')
    
#     options = {
#     'page-size': 'Letter',
#     'margin-top': '0.75in',
#     'margin-right': '0.75in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.75in',
#     'encoding': "UTF-8",
#     'no-outline': None
# }

# pdfkit.from_url('http://google.com', 'out.pdf', options=options)
#     response = HttpResponse(pdf,content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="reprt.pdf"'
#     return response
   
