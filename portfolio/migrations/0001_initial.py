# Generated by Django 5.1.3 on 2024-12-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PersonalInfo",
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
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField()),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="profile/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="projects/"),
                ),
                ("demo_url", models.URLField(blank=True, null=True)),
                ("code_url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
