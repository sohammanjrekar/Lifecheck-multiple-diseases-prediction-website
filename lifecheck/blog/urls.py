from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")
]
