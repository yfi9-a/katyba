# Generated by Django 2.1.5 on 2019-08-15 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armydbapp', '0039_auto_20190723_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_officer',
            name='current_punishment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='armydbapp.Sub_officerPunishments'),
        ),
    ]
