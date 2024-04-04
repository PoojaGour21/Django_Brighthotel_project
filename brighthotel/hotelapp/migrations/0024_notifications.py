# Generated by Django 4.2.4 on 2023-12-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0023_alter_booking_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(default=0, upload_to='')),
            ],
            options={
                'db_table': 'Notifications',
            },
        ),
    ]
