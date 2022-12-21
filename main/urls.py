from django.urls import path, include
from . import views
from .views import Registration, DeleteAdvertView, AdvertView, ApproveAdvertView

urlpatterns = [
    path("", views.start, name="start"),
    path("", include('django.contrib.auth.urls'), name="authentication"),
    path("registration/", Registration.as_view(), name="registration"),
    path("about_us/", views.about_us_page, name="about_us"),
    path("add_animals/", views.add_animals_page, name="add_animals"),
    path("add_animals/upload/", views.add_animals_upload, name="add_animals_upload"),
    path("show_animals/", views.show_animals_page, name="show_animals"),
    path("<pk>/", AdvertView.as_view(), name="full_advert"),
    path("<pk>/approve_advert/", ApproveAdvertView.as_view(), name="approve_advert.html"),
    path("<pk>/delete_advert/", DeleteAdvertView.as_view(), name="delete_advert"),
]
