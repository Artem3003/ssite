# Generated by Django 3.1.4 on 2021-02-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='released',
            field=models.DateTimeField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
