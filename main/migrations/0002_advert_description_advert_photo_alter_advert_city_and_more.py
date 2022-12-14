# Generated by Django 4.1.3 on 2022-12-12 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="advert",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="advert",
            name="photo",
            field=models.FileField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="advert",
            name="city",
            field=models.CharField(choices=[("KV", "Kyiv")], max_length=50),
        ),
        migrations.AlterField(
            model_name="advert",
            name="created",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="advert",
            name="inspector",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="advert",
            name="last_updated",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="advert",
            name="status",
            field=models.CharField(
                choices=[("IN_PROCESS", "In process"), ("DONE", "Done")],
                default="IN_PROCESS",
                max_length=10,
            ),
        ),
    ]