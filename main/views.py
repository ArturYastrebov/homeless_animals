from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from main.forms import AnimalForm, UserCreationForm


# from main.forms import AnimalForm, AddAnimalForm


# Create your views here.


def start(response):
    return render(response, "homeless_animals/start.html")


def show_animals_page(response):
    return render(response, "homeless_animals/show_animals.html")


def about_us_page(response):
    return render(response, "homeless_animals/about_us.html")


def add_animals_page(request):
    form = AnimalForm()
    return render(request, 'homeless_animals/add_animals.html', {'form': form})


def login_user(response):
    return render(response, "registration/login.html")


class Registration(View):

    templates_name = 'registration/registration.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.templates_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.templates_name, context)



