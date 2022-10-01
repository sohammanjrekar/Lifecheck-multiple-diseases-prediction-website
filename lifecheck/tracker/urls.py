from django.contrib import admin
from django.urls import path
from tracker import views
urlpatterns = [
    path('', views.calorie, name="calorie"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
]