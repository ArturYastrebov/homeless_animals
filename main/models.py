from django.utils import timezone
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
    SEX_CHOICES = [("Male", "Male"), ("Female", "Female")]
    AGE_CHOICES = [
        ("JN", "Junior"),
        ("MD", "Middle"),
        ("SN", "Senior"),
    ]

    LOST_CHOICES = [("YES", "Yes"), ("No", "No")]
    species = models.CharField(max_length=3, choices=SPECIES_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    lost = models.CharField(max_length=3, choices=LOST_CHOICES)

    def __str__(self):
        return f"species: {self.species}\nsize: {self.size}\nsex: {self.sex}\nage: {self.age}\nlost: {self.lost}"


class CustomUser(AbstractUser):

    phone_number = models.IntegerField(null=True)


class Advert(models.Model):
    STATUS_CHOICES = [("IN_PROCESS", "In process"), ("DONE", "Done")]

    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(blank=True, default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="IN_PROCESS"
    )
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    photo = models.FileField(default="")
    city = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    description = models.TextField(default="")
    inspector = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)

    def __str__(self):
        return f" last_update: {self.last_updated}\ncity: {self.city}\ncoordinates\n{self.coordinates}\ndescription: {self.description}"
