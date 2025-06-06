# Generated by Django 4.2.20 on 2025-04-22 01:03

from django.db import migrations, models
import django.db.models.deletion


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
                ("title", models.CharField(max_length=100)),
                ("developer", models.CharField(max_length=100)),
                ("platform", models.CharField(default="null", max_length=50)),
                ("slug", models.SlugField(default="null", max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Tags",
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
                ("label", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("review", models.CharField(max_length=1000)),
                ("date", models.DateField(auto_now=True)),
                ("slug", models.SlugField(default="null", max_length=150)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gamereview.game",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="label_tag",
            field=models.ManyToManyField(to="gamereview.tags"),
        ),
    ]
