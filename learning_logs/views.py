from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    """The home page for learning log"""
    return render(request, "index.html")

@login_required(login_url='users:login')
def topics(request):
    #Showing all the topics:
    topics = Topic.objects.filter(owner=request.user).order_by("date_added") #Querying the database and requesting the queryset in topics
    #This is the context that we will be sending to the template:
    context = {"topics": topics} #Contains the set of topics that will be listed on the page
    return render(request, "topics.html", context)

@login_required(login_url='users:login')
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    #Making sure that the topic belongs to the current user:
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added') #Sorting entries by date added and making sure topics are exclusive to user
    context = {'topic': topic, "entries": entries}
    return render(request, "topic.html", context)

@login_required(login_url='users:login')
def new_topic(request):
    #Adding a new topic by the user:
    if request.method != "POST":
        #If there is not data submitted, then create a blank form
        form = TopicForm()
    else:
        #If there is a POST requestm then the data needs to be processed
        form = TopicForm(data = request.POST) #storing data that is stored in request.POST
        if form.is_valid(): #Checking whether or not all fields have been validly filled out
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_logs:topics")
    
    #Displaying a blank or invalid form:
    context = {"form": form}
    return render(request, "new_topic.html", context)

#This method will be called when user wants to add an entry w/o admin page
@login_required(login_url='users:login')
def new_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)

    if request.method != "POST":
        #If there is no data submitted, then create a blank entry form:
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False) #Need to tell Django to create a new object without sending it into database
            new_entry.topic = topic
            new_entry.save() #Saving entry to database with correct associated topic
            return redirect("learning_logs:topic", topic_id = topic_id)
    
    context = {"topic": topic, "form": form}
    return render(request, "new_entry.html", context)

@login_required(login_url='users:login')
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic 
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry) #Django pulls up preexisting information for this entry
    else:
        #POST data submitted; process data
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id = topic.id)
    
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "edit_entry.html", context)




    
