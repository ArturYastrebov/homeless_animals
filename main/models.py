from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class Animal(models.Model):
    SPECIES_CHOICES = [
        ("DOG", "Dog"),
        ("CAT", "Cat"),
    ]
    SIZE_CHOICES = [
        ("L", "Big"),
        ("M", "Middle"),
        ("S", "Small"),
    ]
    SEX_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female")
    ]
    AGE_CHOICES = [
        ("JN", "Junior"),
        ("MD", "Middle"),
        ("SN", "Senior"),
    ]

    LOST_CHOICES = [
        ("YES", "Yes"),
        ("No", "No")
    ]


    species = models.CharField(max_length=3, choices=SPECIES_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    lost = models.CharField(max_length=3, choices=LOST_CHOICES)


class CustomUser(AbstractUser):

    phone_number = models.IntegerField(null=True)

class Advert(models.Model):
    STATUS_CHOICES = [
        ("IN_PROCESS", "In process"),
        ("DONE", "Done")
    ]


    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(blank=True, auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    description = models.TextField(default="")
    inspector = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
