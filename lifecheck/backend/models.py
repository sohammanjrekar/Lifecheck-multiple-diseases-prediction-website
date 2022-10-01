from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.contrib.postgres.fields import ArrayField

class symptom(models.Model):
    symptom_name  = models.CharField(max_length = 100)
    symptom_id = models.IntegerField()
    def __str__(self):
        return self.symptom_name
    
class disease(models.Model):
    symptoms = models.ForeignKey(symptom, null=True, on_delete=models.SET_NULL)
    disease_name = models.CharField(max_length = 100)
    no_of_symp = models.IntegerField()
    symptom_name = ArrayField(models.CharField(max_length=200))
    def __str__(self):
        return self.disease_name
    
class Patient(models.Model):
    patient_id=models.AutoField
    patient_name=models.CharField(max_length=50)
    dob = models.DateField()
    disease = models.ForeignKey(disease, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    email = models.CharField(max_length=111)
    gender = models.CharField(max_length = 10)
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
    
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=150, default="")
    def __str__(self):
        return self.name