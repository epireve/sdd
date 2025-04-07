# Generated by Django 5.2 on 2025-04-07 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
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
        migrations.AlterModelOptions(
            name="game",
            options={},
        ),
        migrations.RenameField(
            model_name="game",
            old_name="genre",
            new_name="developer",
        ),
        migrations.RemoveField(
            model_name="game",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="game",
            name="description",
        ),
        migrations.RemoveField(
            model_name="game",
            name="publisher",
        ),
        migrations.RemoveField(
            model_name="game",
            name="rating",
        ),
        migrations.RemoveField(
            model_name="game",
            name="release_date",
        ),
        migrations.RemoveField(
            model_name="game",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="game",
            name="platform",
            field=models.CharField(default="null", max_length=50),
        ),
        migrations.AddField(
            model_name="game",
            name="slug",
            field=models.SlugField(default="null", max_length=150),
        ),
        migrations.AlterField(
            model_name="game",
            name="title",
            field=models.CharField(max_length=100),
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
                        on_delete=django.db.models.deletion.CASCADE, to="games.game"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="label_tag",
            field=models.ManyToManyField(to="games.tags"),
        ),
    ]
