# Generated by Django 5.0 on 2024-02-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("class_schedule", "0020_alter_classgym_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classgym",
            name="title",
            field=models.CharField(
                choices=[
                    ("zumba", "Zumba"),
                    ("crossfit", "Crossfit"),
                    ("trx", "Trx"),
                    ("bodypump", "Bodypump"),
                    ("cycling", "Cycling"),
                    ("aerobic", "Aerobic"),
                ],
                max_length=8,
            ),
        ),
    ]
