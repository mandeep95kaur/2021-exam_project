# Generated by Django 2.2 on 2021-06-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0002_auto_20210625_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
    ]
