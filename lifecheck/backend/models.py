from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.contrib.postgres.fields import ArrayField


    
class disease(models.Model):
    disease_name = models.CharField(max_length = 100)
    no_of_symp = models.IntegerField()
    symptom_name = ArrayField(models.CharField(max_length=200))
    
    def __str__(self):
        return self.disease_name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=150, default="")
    def __str__(self):
        return self.name
    
class symptom(models.Model):
    symp_name  = models.CharField(max_length = 100)
    disease = models.OneToOneField(disease, on_delete=models.CASCADE, primary_key=True)
    symptom_id = models.AutoField
    
class Patient(models.Model):
    GENDER_CHOICES = (
    ('1', 'Male'),
    ('2', 'Female'),
    ('3', 'Others'),
    )
    patient_id=models.AutoField
    patient_name=models.CharField(max_length=50)
    dob = models.DateField()
    disease = models.OneToOneField(disease, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    email = models.CharField(max_length=111)
    gender = models.CharField(max_length=25,choices=GENDER_CHOICES)
    doctor_name=models.CharField(max_length=50)
    join_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="backend/images",default="")
    
    def __str__(self):
        return self.patient_name

    
    @property
    def age(self):
        today = date.today()
        db = self.dob
        age = today.year - db.year
        if today.month < db.month or today.month == db.month and today.day < db.day:
            age -= 1
        return age 
    
    
