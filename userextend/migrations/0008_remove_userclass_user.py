# Generated by Django 5.0 on 2024-02-06 17:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userextend", "0007_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userclass",
            name="user",
        ),
    ]
