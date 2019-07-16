from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for learning log"""
    return render(request, "index.html")

def topics(request):
    #Showing all the topics:
    topics = Topic.objects.order_by("date_added") #Querying the database and requesting the queryset in topics
    #This is the context that we will be sending to the template:
    context = {"topics": topics} #Contains the set of topics that will be listed on the page
    return render(request, "topics.html", context)