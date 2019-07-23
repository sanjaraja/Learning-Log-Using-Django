from django.shortcuts import render, redirect 

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("learning_logs:index")