from django.urls import path
from . import views

urlpatterns = [
    path('user_information/<int:pk>',views.success,name='user_information'),
    # path('new/message/',views.newMessage),
    # path('new/comment/',views.newComment),
    # path('delete/message/<int:pk>/',views.delete)
]