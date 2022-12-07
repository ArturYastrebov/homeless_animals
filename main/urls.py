from django.urls import path
from . import views


urlpatterns = [
    path("", views.start, name="start"),
    path("add_animals/", views.add_animals_page, name="add_animals"),
    path("show_animals/", views.open_animals_page, name="show_animals"),
    path("about_us/", views.about_us_page, name="about_us"),
    path("add_animals/upload/", views.add_animals_upload, name="upload"),
    # path("show_animals/<id:int>", views.show_proper_animals, name="proper_animals")
]
