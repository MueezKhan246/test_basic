from django.shortcuts import render
# from .forms import TaskForm
from django.contrib.auth.models import User
# Create your views here.

def list_tasks(request):
    

    return render(request, "index.html", {
        "Users" : User.objects.count()
    })