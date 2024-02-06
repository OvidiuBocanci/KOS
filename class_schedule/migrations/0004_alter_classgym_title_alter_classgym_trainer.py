# Generated by Django 5.0 on 2024-02-01 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("class_schedule", "0003_alter_classgym_title_alter_classgym_trainer"),
        ("prices", "0005_alter_card_benefit_2_alter_card_benefit_3_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classgym",
            name="title",
            field=models.CharField(
                choices=[
                    ("cycling", "CYCLING"),
                    ("zumba", "ZUMBA"),
                    ("bodypump", "BODYPUMP"),
                    ("crossfit", "TRAINING"),
                    ("aerobic", "AEROBIC"),
                    ("trx", "TRX"),
                ],
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="classgym",
            name="trainer",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                to="prices.card",
            ),
        ),
    ]
