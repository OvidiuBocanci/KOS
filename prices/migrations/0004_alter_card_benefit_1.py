# Generated by Django 5.0 on 2024-01-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prices", "0003_alter_card_benefit_1_alter_card_benefit_2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="benefit_1",
            field=models.CharField(blank=True, default="none", max_length=50),
            preserve_default=False,
        ),
    ]