from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<file>",views.entry,name="entry"),
    path("random/",views.rando,name="random")
]
