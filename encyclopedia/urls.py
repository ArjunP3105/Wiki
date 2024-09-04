from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>",views.entry,name = "entry"),
    path("search/",views.search,name="search"),
    path("new/",views.new_page,name="new"),
    path("edit_content/",views.edit_content,name="edit_content"),
    path("edit/",views.edit,name="edit"),
    path("rand/",views.randomizer,name="randomizer")
]
