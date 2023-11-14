from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('/', views.index, name="home"),
    path('home/', views.index, name="home"),
    path('home', views.index, name="home"),
    path('words_list', views.words, name="words"),
    path('words_list/', views.words, name="words"),
    path('add_word', views.add_word, name="add_word"),
    path('add_word/', views.add_word, name="add_word"),
]
