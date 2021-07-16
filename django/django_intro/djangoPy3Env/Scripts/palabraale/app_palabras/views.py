from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def redirect_random_world(request):
    return redirect('/random_world')


def form(request):
    return  render(request, 'index.html')


def random(request):
    # print(request.session['contador'])
    if  'contador' not in request.session:
        print("---------------------------------------------------------------------------")
        request.session['contador'] = 1
        
        # print("inicio", "-"*10)
    else:
         request.session['contador'] += 1
   
    request.session['palabra'] = get_random_string(length=14)
    return  render(request, 'index.html')

def restart(request):
    request.session.clear()
    return render(request, 'index.html')


        

    
