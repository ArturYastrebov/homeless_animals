# Generated by Django 4.1.3 on 2022-12-02 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "species",
                    models.CharField(
                        choices=[("DOG", "Dog"), ("CAT", "Cat")], max_length=3
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[("L", "Big"), ("M", "Middle"), ("S", "Small")],
                        max_length=1,
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=6
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        choices=[
                            ("PUPPY", "Puppy"),
                            ("KITTEN", "Kitten"),
                            ("ADULT_DOG", "Adult dog"),
                            ("ADULT_CAT", "Adult cat"),
                        ],
                        max_length=9,
                    ),
                ),
                ("lost", models.BooleanField(verbose_name=False)),
            ],
            options={
                "db_table": "animal",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nick_name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("phone_number", models.IntegerField(max_length=16)),
                ("password", models.CharField(max_length=20)),
                ("permission", models.BooleanField(verbose_name=False)),
            ],
            options={
                "db_table": "user",
            },
        ),
        migrations.CreateModel(
            name="Advert",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("IN_PROCESS", "In process"), ("DONE", "Done")],
                        max_length=10,
                    ),
                ),
                ("sity", models.CharField(max_length=50)),
                ("coordinates", models.CharField(max_length=50)),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="main.animal"
                    ),
                ),
                (
                    "inspector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="main.user"
                    ),
                ),
            ],
            options={
                "db_table": "advert",
            },
        ),
    ]
