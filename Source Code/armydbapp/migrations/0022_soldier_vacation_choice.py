# Generated by Django 2.1.5 on 2019-04-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armydbapp', '0021_auto_20190426_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldier',
            name='vacation_choice',
            field=models.IntegerField(blank=True, default='1', null=True),
        ),
    ]
