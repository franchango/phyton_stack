from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_book', views.new_book),
    path('books/<int:book_id>', views.view_book),
    path('add_author', views.add_author),
    path('authors', views.authors),
    path('new_author', views.new_author),
    path('authors/<int:author_id>', views.view_author),
    path('add_book', views.add_book),
]