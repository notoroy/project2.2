from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>" , views.entrypage , name="entrypage"),
    path("search/" ,views.search , name="search"),
    path("new/", views.new , name="new"), 
    path("edit/",views.edit ,name="edit"),
    path("save/" , views.save , name="save"),
    path("random/" ,views.random_choice , name="randomchoice"),  
]