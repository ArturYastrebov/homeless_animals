from django.urls import path

from google_maps.views import AnimalView

urlpatterns = [
    path("api/v1/animals/", AnimalView.as_view()),
]