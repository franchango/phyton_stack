from django.urls import path
from . import views

urlpatterns = [
    path('wall/',views.success),
    path('new/message/',views.newMessage),
    path('new/comment/',views.newComment),
    path('delete/message/<int:pk>/',views.delete)
]