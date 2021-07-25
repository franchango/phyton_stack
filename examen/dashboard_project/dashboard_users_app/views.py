import re
from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'home.html')

def signin(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/signin/')
        else:
            logged_user = User.objects.get(email=request.POST['email'])
            request.session['logged_user'] = logged_user.id
            return redirect('/dashboard/')
    return render(request,'signin.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.form_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            user_level = 0
            if User.objects.all():
                user_level = 1
            else:
                user_level = 9
            User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],password=pw_hash,user_level=user_level)
            messages.success(request, 'Usuario creado correctamente! Puede iniciar sesion!')
            return redirect('/register/')
    return render(request,'register.html')

def add_user(request):
    if "logged_user" not in request.session:
        print("QUE CHUCHA PASA? HAY SESION?")
        messages.error(request,"There is not logged user!! Log in first!")
        return redirect('/')
    if request.method == "POST":
        errors = User.objects.form_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/add_user/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            user_level = 0
            if User.objects.all():
                user_level = 1
            else:
                user_level = 9
            User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],password=pw_hash,user_level=user_level)
            messages.success(request, 'Usuario creado correctamente! Puede iniciar sesion!')
            return redirect('/add_user/')
    return render(request,'add_user.html')

def dashboard(request):
    if "logged_user" not in request.session:
        print("QUE CHUCHA PASA? HAY SESION?")
        messages.error(request,"There is not logged user!! Log in first!")
        return redirect('/')
    logged_user_level = User.objects.get(id=request.session['logged_user']).user_level
    all_users = User.objects.all()
    context = {
        'all_users' : all_users,
        'logged_user_level' : logged_user_level
    }   
    return render(request,'dashboard.html',context)

def deleteUser(request,pk):
    usr_to_del = User.objects.get(id =pk)
    usr_to_del.delete()
    return redirect('/dashboard/')

def editUser(request,pk):
    if "logged_user" not in request.session:
        messages.error(request,"There is not logged user!! Log in first!")
        return redirect('/')
    if request.method == "POST":
        user_to_edit = User.objects.get(id=pk)
        if request.POST['update_type'] == 'usr':
            errors = User.objects.form_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect('/edit_user/'+str(pk))
            else:
                user_to_edit.email = request.POST['email']
                user_to_edit.fname = request.POST['fname']
                user_to_edit.lname = request.POST['lname']
                user_to_edit.user_level = request.POST['user_level']
                user_to_edit.save()
                return redirect('/dashboard/')
        if request.POST['update_type'] == 'pwrd':
            errors = User.objects.form_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect('/edit_user/'+str(pk))
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
                user_to_edit.password = pw_hash
                user_to_edit.save()
                return redirect('/dashboard/')
    usr_to_edit = User.objects.get(id=pk)
    logged_user_level = User.objects.get(id=request.session['logged_user']).user_level
    context = {
        'usr_to_edit' : usr_to_edit,
        'logged_user_level' : logged_user_level
    }
    return render(request,'edit_user.html',context)

def editProfile(request,pk):
    if "logged_user" not in request.session:
        messages.error(request,"There is not logged user!! Log in first!")
        return redirect('/')
    if request.method == "POST":
        user_to_edit = User.objects.get(id=pk)
        if request.POST['update_type'] == 'usr':
            errors = User.objects.form_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect('/edit_profile/'+str(pk))
            else:
                user_to_edit.email = request.POST['email']
                user_to_edit.fname = request.POST['fname']
                user_to_edit.lname = request.POST['lname']
                user_to_edit.save()
                return redirect('/dashboard/')
        if request.POST['update_type'] == 'pwrd':
            errors = User.objects.form_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect('/edit_profile/'+str(pk))
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
                user_to_edit.password = pw_hash
                user_to_edit.save()
                return redirect('/dashboard/')
    usr_to_edit = User.objects.get(id=pk)
    logged_user_level = User.objects.get(id=request.session['logged_user']).user_level
    context = {
        'usr_to_edit' : usr_to_edit,
        'logged_user_level' : logged_user_level
    }
    return render(request,'edit_profile.html',context)

def addDescription(request):
    add_desc = User.objects.get(id=request.POST['desc_usr_id'])
    add_desc.description = request.POST['description']
    add_desc.save()
    return redirect('/dashboard/')

def logout(request):
    request.session.flush()
    return redirect('/')
    