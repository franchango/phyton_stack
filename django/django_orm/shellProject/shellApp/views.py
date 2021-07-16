from django.shortcuts import redirect, render
from shellApp.models import *

def index(request):
    context = {
        'all_users': User.objects.all()
    }
    print(context['all_users'])
    return render(request, 'index.html', context)

def creat_users(request):
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age'],
    )
    return redirect('/')