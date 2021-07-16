"""firt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path     
from . import views
urlpatterns = [
     #/ - redirige a la ruta "/blogs" con el método llamado "root"
    path('',views.root),

    #/blogs - muestra el string "placeholder para luego mostrar una lista de todos los blogs" con un método llamado "index"
    path('blogs',views.index),
    
    #/blogs/new - muestra el string "placeholder para mostrar un nuevo formulario para crear un nuevo blog" con un método llamado "new"
    path('new', views.new),

    #/blogs/create - redirige a la ruta "/" con un método llamado "create"
    path('create', views.create),

    #/blogs/< number > - muestra el string "placeholder para mostrar el blog numero: {number}" con un método llamado "show" (ej. localhost:8000/blogs/15 debería mostrar el mensaje: 'placeholder para mostrar el blog numero 15')
    path('<int:num>', views.show),

    #/blogs/< number >/edit - muestra el string "placeholder para editar el blog {number}" con un método llamado "edit"
    path('<int:num>/edit', views.edit),

    #/blogs/< number >/delete - redirige a la ruta "/blogs" con el método llamado "destroy"
    path('<int:num>/delete', views.destroy),

    #(**Bonus**) /blogs/json - regresa una JsonResponse con un titulo y que contenga llaves.
    path('json', views.json)    
]
