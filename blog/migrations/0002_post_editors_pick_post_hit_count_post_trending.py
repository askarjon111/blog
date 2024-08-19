# Generated by Django 5.1 on 2024-08-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="editors_pick",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="post",
            name="hit_count",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="trending",
            field=models.BooleanField(default=False),
        ),
    ]
