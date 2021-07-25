from django.urls import path
from . import views
from dashboard_messages_app import urls

urlpatterns = [
    path('',views.index,name='home'),
    path('signin/',views.signin, name='signin'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('add_user/',views.add_user, name='add_user'),
    path('del_user/<int:pk>',views.deleteUser, name='del_user'),
    path('edit_user/<int:pk>',views.editUser, name='edit_user'),
    path('edit_profile/<int:pk>',views.editProfile, name='edit_profile'),
    path('add_desc/',views.addDescription, name='add_desc')
    
]