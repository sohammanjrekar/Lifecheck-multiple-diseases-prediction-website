from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="About"),
    path('blog/',views.blog,name="Blog"),
    path('contact/',views.contact,name="Contact"),
]