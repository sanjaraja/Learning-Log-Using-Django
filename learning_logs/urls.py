#Need to define url patterns for learning_logs:
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #This is the home page
    path('', views.index, name = "index"),

    #This will show the topics:
    path('topics', views.topics, name = "topics")
]

