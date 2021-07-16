from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addCourse', views.addCourse),
    path('destroy/<int:id>', views.confirmDestroy),
    path('destroyCourse/<int:id>', views.destroyCourse)
]