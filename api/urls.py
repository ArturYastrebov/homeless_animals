from django.urls import path

from api.views import AnimalView

urlpatterns = [
    path("api/v1/animals/", AnimalView.as_view()),
]