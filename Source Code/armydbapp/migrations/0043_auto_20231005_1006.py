# Generated by Django 2.1.5 on 2023-10-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armydbapp', '0042_soldier_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='point',
            field=models.CharField(max_length=256),
        ),
    ]
