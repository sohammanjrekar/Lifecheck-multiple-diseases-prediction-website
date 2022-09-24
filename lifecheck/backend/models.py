from django.db import models

# Create your models here.
class Patients(models.Model):
    patient_id=models.AutoField
    patient_name=models.CharField(max_length=50)
    Age=models.IntegerField(default=0)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    email = models.CharField(max_length=111)
    doctor_name=models.CharField(max_length=50)
    join_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="backend/images",default="")
    def __str__(self):
        return self.patient_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name