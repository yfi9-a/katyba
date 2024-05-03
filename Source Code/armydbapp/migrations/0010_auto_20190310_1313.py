# Generated by Django 2.1.5 on 2019-03-10 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armydbapp', '0009_soldier_soldier_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_days', models.IntegerField(blank=True, null=True)),
                ('reward_date', models.DateField(blank=True, null=True)),
                ('soldier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armydbapp.Soldier')),
            ],
        ),
        migrations.AddField(
            model_name='soldierarmyunits',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]