# Generated by Django 5.0 on 2024-02-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("class_schedule", "0041_alter_classgym_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classgym",
            name="title",
            field=models.CharField(
                choices=[
                    ("cycling", "Cycling"),
                    ("crossfit", "Crossfit"),
                    ("bodypump", "Bodypump"),
                    ("aerobic", "Aerobic"),
                    ("zumba", "Zumba"),
                    ("trx", "Trx"),
                ],
                max_length=8,
            ),
        ),
    ]
