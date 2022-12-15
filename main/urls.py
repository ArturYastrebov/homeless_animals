from django.urls import path, include
from . import views
from .views import Registration, UploadAnimalPoint

urlpatterns = [
    path("", views.start, name="start"),
    path("add_animals/", UploadAnimalPoint.as_view(), name="add_animals_points"),
    path("show_animals/", views.show_animals_page, name="show_animals"),
    path("about_us/", views.about_us_page, name="about_us"),
    path("", include('django.contrib.auth.urls'), name="authentication"),
    path("registration/", Registration.as_view(), name="registration"),
    path("upload_animal_point/", views.upload_animal_point, name="upload_animal_point"),
]
