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
        ("PUPPY", "Puppy"),
        ("KITTEN", "Kitten"),
        ("ADULT_DOG", "Adult dog"),
        ("ADULT_CAT", "Adult cat"),
    ]


    class Meta:
        db_table = "animal"

    species = models.CharField(max_length=3, choices=SPECIES_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.CharField(max_length=9, choices=AGE_CHOICES)
    lost = models.BooleanField(False)


class User(models.Model):


    class Meta:
        db_table = "user"

    nick_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=16)
    password = models.CharField(max_length=20)
    permission = models.BooleanField(False)

class Advert(models.Model):
    STATUS_CHOICES = [
        ("IN_PROCESS", "In process"),
        ("DONE", "Done")
    ]


    class Meta:
        db_table = "advert"

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    animal = models.ForeignKey(Animal, on_delete=models.RESTRICT)
    sity = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    description = models.TextField
    inspector = models.ForeignKey(User, on_delete=models.RESTRICT)
