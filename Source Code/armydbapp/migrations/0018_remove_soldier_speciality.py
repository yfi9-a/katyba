# Generated by Django 2.1.5 on 2019-04-25 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armydbapp', '0017_auto_20190425_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldier',
            name='speciality',
        ),
    ]
