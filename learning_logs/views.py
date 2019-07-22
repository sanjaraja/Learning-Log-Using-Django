from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm


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

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added') #Need to sort the entires by most recently added
    context = {'topic': topic, "entries": entries}
    return render(request, "topic.html", context)

def new_topic(request):
    #Adding a new topic by the user:
    if request.method != "POST":
        #If there is not data submitted, then create a blank form
        form = TopicForm()
    else:
        #If there is a POST requestm then the data needs to be processed
        form = TopicForm(request.POST) #storing data that is stored in request.POST
        if form.is_valid(): #Checking whether or not all fields have been validly filled out
            form.save() #Writes data in form to database
            return redirect("topics")
    
    #Displaying a blank or invalid form:
    context = {"form": form}
    return render(request, "new_topic.html", context)



    
