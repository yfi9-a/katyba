# Generated by Django 2.1.5 on 2019-02-19 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armydbapp', '0002_auto_20190219_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='reward_days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
