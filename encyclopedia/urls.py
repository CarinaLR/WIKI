from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create", views.create, name="create"),
    path("wiki/<str:title>", views.entry_page, name="title"),
    path("wiki/random", views.random, name="random")
]
