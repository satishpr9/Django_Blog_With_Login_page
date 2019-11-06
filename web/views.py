from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def index(request):
    obj=Post.objects.all()
    return render (request, "index.html",{'obj':obj})



def signup(request):
    return render(request, "signup.html")

def register(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        obj = User(username=username , email=email , password=password)
        obj.save()
        return redirect(login)
        

  
def login(request):
    if request.POST:
        username=request.POST['username']
        password= request.POST['password']

        count= User.objects.filter(username=username, password=password).count()
        if count > 0:
            
            return redirect(index)
        else:
            messages.error(request,"invalid username and password")
            return redirect(login)
    return render(request, "login.html")



		



