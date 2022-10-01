from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="About"),
    path('blog/',views.blog,name="Blog"),
    path('contact/',views.contact,name="Contact"),
    path('diabetes/',views.diabetes,name="diabetes"),
    path('heart/',views.heart,name="heart"),
    path('parkinsons/',views.parkinsons,name="parkinsons"),
    path('diabetes/result_diabetes',views.result_diabetes,name="result_diabetes"),
]