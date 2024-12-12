from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ('portfolio', '0001_initial'),

    ]

    operations = [
        migrations.AlterField(

            model_name="personalinfo",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/profile.jpeg"
            ),

        ),

    ]
