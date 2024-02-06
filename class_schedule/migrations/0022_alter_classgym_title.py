# Generated by Django 5.0 on 2024-02-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("class_schedule", "0021_alter_classgym_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classgym",
            name="title",
            field=models.CharField(
                choices=[
                    ("trx", "Trx"),
                    ("crossfit", "Crossfit"),
                    ("bodypump", "Bodypump"),
                    ("cycling", "Cycling"),
                    ("aerobic", "Aerobic"),
                    ("zumba", "Zumba"),
                ],
                max_length=8,
            ),
        ),
    ]
