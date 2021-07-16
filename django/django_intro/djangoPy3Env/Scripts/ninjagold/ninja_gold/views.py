from django.shortcuts import render, redirect
from random import randint, choice

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['earn'] = 0
        request.session['move'] = 0
        request.session['activities'] = []
        request.session['activities'].insert(0, "Comienza el Juego")
    return render(request, "index.html")

def process_money(request, location):
    if request.method == "POST":
        if location == "casino":
            request.session['earn'] = randint(0, 50) * choice([-1, 1])
            if request.session['earn'] > 0:
                request.session['activities'].insert(0, f"Ingresó a un casino y ganó {request.session['earn']} oros! ¡Hurra!")
            else:
                request.session['activities'].insert(0, f"Entró en un casino y perdió {-1*request.session['earn']} oros .. Ouch ..")
        else:
            if location == "farm":
                request.session['earn'] = randint(10, 20)
            if location == "cave":
                request.session['earn'] = randint(5, 10)
            if location == "house":
                request.session['earn'] = randint(2, 5)
            request.session['activities'].insert(0, f"Gana {request.session['earn']} oros del {location}!")
        request.session['gold'] += request.session['earn']
        request.session['move'] += 1
    return redirect("/") 

def reset(request):
    del request.session['gold']
    del request.session['earn']
    del request.session['move']
    return redirect("/")