# Generated by Django 5.0.6 on 2024-07-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("poll", "0004_remove_poll_total_votes"),
    ]

    operations = [
        migrations.CreateModel(
            name="voteModel",
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
                ("votes", models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name="choice",
            name="votes",
        ),
    ]
