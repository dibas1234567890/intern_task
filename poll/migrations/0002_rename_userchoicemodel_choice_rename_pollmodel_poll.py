# Generated by Django 5.0.6 on 2024-07-07 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("poll", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="userChoiceModel",
            new_name="Choice",
        ),
        migrations.RenameModel(
            old_name="pollModel",
            new_name="Poll",
        ),
    ]
