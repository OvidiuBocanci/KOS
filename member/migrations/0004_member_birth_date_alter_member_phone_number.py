# Generated by Django 5.0 on 2024-01-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0003_member_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="birth_date",
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="member",
            name="phone_number",
            field=models.IntegerField(),
        ),
    ]
