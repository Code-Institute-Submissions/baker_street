# Generated by Django 3.1.2 on 2020-11-09 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rooms',
            options={'verbose_name_plural': 'Rooms'},
        ),
    ]