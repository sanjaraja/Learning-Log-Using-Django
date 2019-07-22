#Need to define url patterns for learning_logs:
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #This is the home page
    path('', views.index, name = "index"),

    #This will show the topics:
    path('topics/', views.topics, name = "topics"),

    #Seeing an individual topic page:
    path('topic/<int:topic_id>/', views.topic, name = "topic"),

    #Page for user adding a new topic: 
    path("new_topic/", views.new_topic, name = "new_topic"),
]

