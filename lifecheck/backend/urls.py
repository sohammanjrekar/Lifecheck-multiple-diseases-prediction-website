from django.urls import path 
from . import views
from .views import diabetes_report,parkinsons_report,heart_report

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="About"),
    path('blog/',views.blog,name="Blog"),
    path('contact/',views.contact,name="Contact"),
    path('diabetes/',views.diabetes,name="diabetes"),
    path('diabetes/result_diabetes',views.result_diabetes,name="result_diabetes"),
    path('diabetes/report',diabetes_report.as_view()),
    path('heart/',views.heart,name="heart"),
    path('heart/result_heart',views.result_heart,name="result_heart"),
    path('heart/result_heart/report',heart_report.as_view()),
    path('parkinsons/',views.parkinsons,name="parkinsons"),
    path('parkinsons/result_parkinsons',views.result_parkinsons,name="result_parkinsons"),
    path('parkinsons/report',parkinsons_report.as_view()),
    # path('pdf/', diabetes_report.as_view()),
    
]