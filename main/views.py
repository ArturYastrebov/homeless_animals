from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DeleteView, UpdateView, DetailView

from main.forms import UserCreationForm, AddAnimalAdvertForm

from main.forms import FindAnimalAdvertForm
from main.models import AnimalAdvert


# Create your views here.


def start(response):
    return render(response, "homeless_animals/start.html")


def about_us_page(response):
    return render(response, "homeless_animals/about_us.html")


def show_animals_page(request):
    form = FindAnimalAdvertForm()
    return render(request, "homeless_animals/show_animals.html", {"form": form})


def show_animals_upload(request):
    animal_advert_list = AnimalAdvert.objects.all()
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
    return render(request, "homeless_animals/add_animals_upload.html")


def login_user(response):
    return render(response, "registration/login.html")


class Registration(View):

    templates_name = "registration/registration.html"

    def get(self, request):
        context = {"form": UserCreationForm()}
        return render(request, self.templates_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        context = {"form": form}
        return render(request, self.templates_name, context)


class AdvertView(DetailView):
    model = AnimalAdvert
    template_name = "homeless_animals/full_advert.html"
    context_object_name = "advert"


class DeleteAdvertView(DeleteView):
    model = AnimalAdvert
    template_name = "homeless_animals/delete_advert.html"

    def get_success_url(self):
        return reverse("show_animals")


class ApproveAdvertView(UpdateView):
    model = AnimalAdvert
    fields = ["status"]
    template_name_suffix = "_update_form"
    template_name = "homeless_animals/approve_advert.html"

    def get_success_url(self):
        return reverse("show_animals")
