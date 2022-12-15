from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from main.models import AnimalPoint


# Create your views here.
class AnimalView(View):

    def get(self, request):
        return JsonResponse({'animals': [model_to_dict(m) for m in AnimalPoint.objects.all()]})
