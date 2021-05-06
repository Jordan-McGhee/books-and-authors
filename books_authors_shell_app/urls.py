from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('books/<int:id>', views.show_book),
    path('books/create', views.create_book),
    path('books/<int:id>/addauthor', views.add_author),
    path('authors', views.authors),
    path('authors/<int:id>', views.show_author),
    path('authors/create', views.create_author),
    path('authors/<int:id>/addbook', views.add_book)
]