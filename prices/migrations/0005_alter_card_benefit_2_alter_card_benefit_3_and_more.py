# Generated by Django 5.0 on 2024-01-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prices", "0004_alter_card_benefit_1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="benefit_2",
            field=models.CharField(blank=True, default="none", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="card",
            name="benefit_3",
            field=models.CharField(blank=True, default="none", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="card",
            name="benefit_4",
            field=models.CharField(blank=True, default="none", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="card",
            name="benefit_5",
            field=models.CharField(blank=True, default="none", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="card",
            name="benefit_6",
            field=models.CharField(blank=True, default="none", max_length=50),
            preserve_default=False,
        ),
    ]
