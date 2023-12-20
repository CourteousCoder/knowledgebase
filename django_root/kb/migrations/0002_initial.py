# Generated by Django 4.2.7 on 2023-12-14 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("kb", "0001_initial"),
        ("pd_data", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="assetgroup",
            name="practiceAreas",
            field=models.ManyToManyField(blank=True, to="pd_data.practicearea"),
        ),
        migrations.AddField(
            model_name="assetgroup",
            name="tools",
            field=models.ManyToManyField(blank=True, to="pd_data.tool"),
        ),
        migrations.AlterUniqueTogether(
            name="assetgroupauthor",
            unique_together={("assetGroup", "author")},
        ),
        migrations.AlterUniqueTogether(
            name="assetgroup",
            unique_together={("slug", "phase")},
        ),
    ]