# Generated by Django 5.0.6 on 2024-07-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("poll", "0002_rename_userchoicemodel_choice_rename_pollmodel_poll"),
    ]

    operations = [
        migrations.AddField(
            model_name="poll",
            name="total_votes",
            field=models.IntegerField(default=0),
        ),
    ]
