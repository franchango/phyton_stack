from django.urls import path     
from . import views
urlpatterns = [
    path('', views.redirect_random_world),	 
    path('random_world', views.form) ,
    path('generate_random', views.random) ,
    path('reset', views.restart)
]