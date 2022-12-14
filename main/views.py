from PIL import Image
import itertools

from django.shortcuts import render
from django.core.paginator import Paginator

from main.forms import AddAnimalAdvertForm, FindAnimalAdvertForm
from main.models import AnimalAdvert


# Create your views here.


def start(response):
    return render(response, "homeless_animals/start.html")


def about_us_page(response):
    return render(response, "homeless_animals/about_us.html")


def show_animals_page(request):
    form = FindAnimalAdvertForm()
    return render(request, "homeless_animals/add_animals.html", {"form": form})


def show_animals_upload(request):
    filters = {key: request.POST.get(key) for key in ["city", "species", "size", "sex", "age", "lost"] if request.POST.get(key) != "---"}
    animal_advert_list = AnimalAdvert.objects.filter(**filters)
    paginator = Paginator(animal_advert_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "homeless_animals/show_animals_upload.html", {"page_obj": page_obj}
    )


def add_animals_page(request):
    form = AddAnimalAdvertForm()
    return render(request, "homeless_animals/add_animals.html", {"form": form})


def add_animals_upload(request):
    if request.method == "POST":
        form = AddAnimalAdvertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, "homeless_animals/upload.html")
