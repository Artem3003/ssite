# Generated by Django 3.1.4 on 2021-02-22 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssite', '0003_remove_track_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='released',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 22, 15, 0, 26, 631825)),
            preserve_default=False,
        ),
    ]
