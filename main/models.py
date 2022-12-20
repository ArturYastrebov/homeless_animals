from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    STATUS_CHOICES = [("REGISTERED", "Registered"), ("VOLUNTEER", "Volunteer")]

    phone_number = models.IntegerField(null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="REGISTERED"
    )


class AnimalAdvert(models.Model):
    STATUS_CHOICES = [("IN_PROCESS", "In process"), ("DONE", "Done")]
    CITY_CHOICES = [
        ("KV", "Kyiv"),
    ]
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

    created = models.DateField(auto_now_add=True)
    last_updated = models.DateField(blank=True, default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="IN_PROCESS"
    )
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    coordinates = models.JSONField(max_length=100, null=False)
    description = models.TextField(null=True)
    inspector = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=True)
    photo = models.ImageField(upload_to="images/", null=True)
    species = models.CharField(max_length=3, choices=SPECIES_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    lost = models.CharField(max_length=3, choices=LOST_CHOICES)
