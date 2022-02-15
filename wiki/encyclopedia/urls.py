from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<file>",views.entry,name="entry"),
    path("random/",views.rando,name="random"),
    path("create",views.createPage,name="create_page"),
    path('wiki/<file>/edit',views.edit,name="edit_page")
]
