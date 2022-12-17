from django.urls import path
from . import views
from .views import Registration


urlpatterns = [
    path("", views.start, name="start"),
    path("add_animals/", views.add_animals_page, name="add_animals"),
    path("show_animals/", views.show_animals_page, name="show_animals"),
    path("about_us/", views.about_us_page, name="about_us"),
    path("add_animals/upload/", views.add_animals_upload, name="add_animals_upload"),
    path("show_animals/upload/", views.show_animals_upload, name="show_animals_upload"),
    path("", include('django.contrib.auth.urls'), name="authentication"),
    path("registration/", Registration.as_view(), name="registration"),
]
