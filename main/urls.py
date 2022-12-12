from django.urls import path, include
from . import views
from .views import Registration

urlpatterns = [
    path("", views.start, name="start"),
    path("add_animals/", views.add_animals_page, name="add_animals"),
    path("show_animals/", views.show_animals_page, name="show_animals"),
    path("about_us/", views.about_us_page, name="about_us"),
    path("", include('django.contrib.auth.urls'), name="authentication"),
    path("registration/", Registration.as_view(), name="registration"),
]
