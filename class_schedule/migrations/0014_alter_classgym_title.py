# Generated by Django 5.0 on 2024-02-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("class_schedule", "0013_rename_user_classgym_trainer_alter_classgym_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classgym",
            name="title",
            field=models.CharField(
                choices=[
                    ("zumba", "ZUMBA"),
                    ("crossfit", "CROSSFIT"),
                    ("aerobic", "AEROBIC"),
                    ("trx", "TRX"),
                    ("Bodypump", "BODYPUMP"),
                    ("cycling", "CYCLING"),
                ],
                max_length=8,
            ),
        ),
    ]