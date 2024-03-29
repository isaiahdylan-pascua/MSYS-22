# Generated by Django 4.2.1 on 2023-07-31 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
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
                ("name", models.CharField(max_length=300)),
                ("city", models.CharField(max_length=300)),
                ("country", models.CharField(max_length=300)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="WaterBottle",
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
                ("sku", models.CharField(max_length=10, unique=True)),
                ("brand", models.CharField(max_length=100)),
                ("size", models.CharField(max_length=50)),
                ("mouth_size", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
                ("current_quant", models.IntegerField(default=0)),
                (
                    "supplied_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Myinventoryapp.supplier",
                    ),
                ),
            ],
        ),
    ]
