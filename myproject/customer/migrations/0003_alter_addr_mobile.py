# Generated by Django 5.0.6 on 2024-06-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_rename_address_addr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addr',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
