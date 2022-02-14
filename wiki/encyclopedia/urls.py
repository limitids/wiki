from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:file>",views.entry,name="Entry"),
    path("random/",views.rando,name="random")
]
