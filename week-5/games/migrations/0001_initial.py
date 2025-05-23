# Generated by Django 5.2 on 2025-04-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("genre", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                ("publisher", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("rating", models.DecimalField(decimal_places=1, max_digits=3)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-release_date"],
            },
        ),
    ]
