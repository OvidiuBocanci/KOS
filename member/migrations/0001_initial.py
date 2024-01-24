# Generated by Django 5.0 on 2024-01-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=6
                    ),
                ),
                ("profile", models.ImageField(null=True, upload_to="profile_members/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
