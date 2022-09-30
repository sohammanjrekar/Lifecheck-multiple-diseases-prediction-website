from django.shortcuts import render
from .models import Patients, Contact

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
    return render(request ,'backend/diabetes.html')



