# Generated by Django 5.1.3 on 2024-12-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinfo",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pics/profile.jpg"
            ),
        ),
    ]
