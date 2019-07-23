from django.shortcuts import render, redirect 

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login

def logout_view(request):
    logout(request)
    return redirect("learning_logs:index")

def register(request):
    if request.method != "POST":
        #Need to display a blank registration form:
        form = UserCreationForm()
    else:
        #Else page needs to take data from user and process a completed form:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save() #Saving user's username and password into database
            login(request, new_user)
            return redirect("learning_logs:index")
    
    #Displaying a blank or invalid form:
    context = {"form": form}
    return render(request, "registration/register.html", context)

            