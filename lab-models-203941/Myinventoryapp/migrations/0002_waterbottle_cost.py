# Generated by Django 4.2.1 on 2023-07-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Myinventoryapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="waterbottle",
            name="cost",
            field=models.FloatField(default=0.0),
        ),
    ]
