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

def process(request):
    print (request.POST)
    errors = User.objects.validator(request.POST)
    if errors:
        for error in errors:
            print (errors[error])
            messages.error(request, errors[error])
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        user = User.objects.create(name = request.POST['name'], email = request.POST['email'], password = hashed_pw, dob = request.POST['date'])
        messages.success(request, "se creo correctamente")
        request.session['id'] = user.id
    return redirect('/')

def login(request):
    login_return = User.objects.login(request.POST)
    if 'user' in login_return:
        request.session['id'] = login_return['user'].id
        messages.success(request, "Has iniciado sesión correctamente")
        return redirect('appoinments.html')
    else:
        messages.error(request, login_return['error clave incorrecta'])
        return redirect('')

def logout(request):
    Session.objects.all().delete()
    return redirect('/')

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
