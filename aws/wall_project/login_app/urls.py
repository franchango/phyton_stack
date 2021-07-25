from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/',views.newUser),
    path('login/',views.login),
    path('logout/',views.logout)  
]