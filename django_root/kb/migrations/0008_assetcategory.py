# Generated by Django 4.2.7 on 2024-01-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kb", "0007_alter_assetgrouptopicarea_asset_group"),
    ]

    operations = [
        migrations.CreateModel(
            name="AssetCategory",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("name", models.CharField(max_length=70, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
