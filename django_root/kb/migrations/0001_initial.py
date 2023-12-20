# Generated by Django 4.2.7 on 2023-12-14 02:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AssetGroup",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
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
                (
                    "google_uuid",
                    models.CharField(default="", max_length=100, unique=True),
                ),
                ("title", models.CharField(default="", max_length=70)),
                ("description", models.CharField(default="", max_length=200)),
                ("slug", models.CharField(default="", max_length=200)),
                ("active", models.BooleanField(default=False)),
                ("published", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
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
                ("email", models.EmailField(max_length=70, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Phase",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
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
        migrations.CreateModel(
            name="PracticeArea",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name="AssetGroupAuthor",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
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
                ("role", models.CharField(default="author", max_length=20)),
                (
                    "assetGroup",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="kb.assetgroup"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="kb.author"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="assetgroup",
            name="phase",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="kb.phase"
            ),
        ),
    ]