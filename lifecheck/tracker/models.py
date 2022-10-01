from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_image=models.ImageField(upload_to="backend/images",default="")
    
    def __str__(self):
        return self.cat_name



class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
    image=models.ImageField(upload_to="backend/images",default="")
    def __str__(self):
        return self.name


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
