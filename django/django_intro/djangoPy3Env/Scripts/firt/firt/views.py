from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Cree sus vistas aquí.
# / - redirecciona a la ruta "/ blogs" con un método llamado "root"
def root(request):
    return redirect("/blogs")

# / blogs: muestra la cadena "marcador de posición para mostrar más tarde una lista de todos los blogs" con un método llamado "índice"
def index(request):
    return HttpResponse("marcador de posición para mostrar más tarde una lista de todos los blogs")

#/ blogs / new: muestra la cadena "marcador de posición para mostrar un nuevo formulario para crear un nuevo blog" con un método llamado "nuevo"
def new(request):
    return HttpResponse("marcador de posición para mostrar un nuevo formulario para crear un nuevo blog")

#/ blogs / create: redirige a la ruta "/" con un método llamado "crear"
def create(request):
    return redirect('/')

#/ blogs / <número>: muestra la cadena "marcador de posición para mostrar el número de blog: {número}" con un método llamado "mostrar" (por ejemplo, localhost: 8000 / blogs / 15 debe mostrar el mensaje: 'marcador de posición para mostrar el número de blog 15 ')
def show(request, num):
    return HttpResponse(f"marcador de posición para mostrar el número de blog: {num}")

#/ blogs / <número> / editar: muestra la cadena "marcador de posición para editar el blog {número}" con un método llamado "editar"
def edit(request, num):
    return HttpResponse(f"marcador de posición para editar el blog{num}")

#/ blogs / <número> / delete: redirige a la ruta "/ blogs" con un método llamado "destruir"
def destroy(request, num):
    return redirect('/blogs')

#(** Bonus **) / blogs / json: devuelve un JsonResponse con claves de título y contenido.
def json(request):
    return JsonResponse({"title":"My first blog", "content":"Lorem ipsum  dolor sit"})