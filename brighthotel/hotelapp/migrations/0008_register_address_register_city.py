# Generated by Django 4.2.4 on 2023-10-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0007_alter_register_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='register',
            name='city',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]