from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry, name="entry" ),
    path("wiki/search/", views.search, name="search")
]
