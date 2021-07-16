from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Course

# Create your views here.

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def addCourse(request):
    errors = Course.objects.custom_form_validator(request.POST)
    if len(errors):
        for key in errors.keys():
            messages.error(request, errors[key])
        return redirect("/")
    else:
        Course.objects.create(name = request.POST["course_name"], description = request.POST["desc"])
        return redirect("/")

def confirmDestroy(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "destroyCourse.html", context)

def destroyCourse(request, id):
    Course.objects.get(id=id).delete()
    return redirect("/")