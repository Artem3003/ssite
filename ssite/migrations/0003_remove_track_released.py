# Generated by Django 3.1.4 on 2021-02-22 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssite', '0002_track_released'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='released',
        ),
    ]