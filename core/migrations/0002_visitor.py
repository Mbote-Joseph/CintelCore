# Generated by Django 4.1 on 2023-08-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visitor",
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
                ("full_name", models.CharField(max_length=100)),
                ("id_number", models.CharField(max_length=20, unique=True)),
                ("phone_number", models.CharField(max_length=15)),
            ],
        ),
    ]
