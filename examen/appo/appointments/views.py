# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt
import datetime
import time
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
today = datetime.date.today()

def index(request):
    return render(request, "index.html")

def process_login(request):
    if request.method =="POST":
        user = User.objects.filter(email= request.POST["email"])
        if user:
            temp_user = user[0]
            if bcrypt.checkpw(request.POST["password"].encode(), temp_user.password.encode()):
                request.session["logged_user"] = temp_user.id
                return redirect("/success")
        messages.error(request, "El email y/o contraseña ingresados no son correctos. Por favor intente nuevamente")
    
    return redirect("/")
def success(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Para acceder a esta página, por favor regístrese y/o ingrese con su usuario")
        return redirect('/')
    context = {
        "logged_user" : User.objects.get(id= request.session["logged_user"]),
    }
    return render(request, "welcome.html", context)

def create_user(request):
    if request.method == "POST":
        # llamada a funcion para validaciones en la capa del modelo
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # método para hacer hash del password
        hash_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hash_password)
        # registro del usuario en la bdd
        new_user = User.objects.create(
            name = request.POST["name"],
            email = request.POST["email"],
            dob=request.POST["dob"],
            password = hash_password
            )
        request.session['logged_user'] = new_user.id

        return redirect('/success')
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")


def appointments(request):

    context = {
        'user': User.objects.get(id=request.session['id']),
        'date': today,
        'appointment': Appointment.objects.filter(date=today),
        'later_appointment': Appointment.objects.exclude(date=today),
    }
    return render(request, "appointments.html", context)

def new_appointment(request):
    # newdate1 = time.strptime(today, "%d/%m/%Y")
    # newdate2 = time.strptime(request.POST['date'], "%d/%m/%Y")
    # if newdate1 < newdate2:
    #     messages.success(request, "Date must be present or greater")
    # else:
    Appointment.objects.create(task=request.POST['task'], date=request.POST['date'], time=request.POST['time'], status="Pending", user_appointments=User.objects.get(id=request.session['id']))
    return redirect('')

def update(request, task_id):
    context = {
        'task': Appointment.objects.get(id=task_id),
    }
    return render(request, "update.html", context)

def change(request, task_id):
    a = Appointment.objects.get(id=task_id)
    a.task=request.POST['task']
    a.date=request.POST['date']
    a.time=request.POST['time']
    a.status=request.POST['status']
    a.save()
    return redirect('')

def delete(request, task_id):
    Appointment.objects.get(id=task_id).delete()
    return redirect('')