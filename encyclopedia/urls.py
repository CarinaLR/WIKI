from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create", views.create, name="create"),
    path("wiki/random_page", views.random_page, name="random_page"),
    path("wiki/edit_page", views.edit_page, name="edit_page"),
    path("wiki/<str:title>", views.entry_page, name="title"),
]
