from typing import ContextManager
from django.db.models.fields import EmailField
from .models import User
from django.shortcuts import redirect, render
from django.urls.conf import include
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request,'index.html')

def  newUser(request):
    if request.method == "POST":
        errors = User.objects.form_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],dob=request.POST['dob'],email=request.POST['email'],password=pw_hash)
            messages.success(request, 'Usuario creado correctamente! Puede iniciar sesion!')
            return redirect('/')
    return redirect("/")

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            logged_user = User.objects.get(email=request.POST['email'])
            request.session['logged_user'] = logged_user.id
            return redirect('/wall/')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')
    
