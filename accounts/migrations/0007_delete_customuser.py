# Generated by Django 4.2.7 on 2023-11-26 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_auto_20231125_2350"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]