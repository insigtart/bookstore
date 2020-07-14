from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("bookslist", views.bookslist, name="listare_carti"),
    path("book/<str:pk>/", views.book, name="fisa carte")
]
