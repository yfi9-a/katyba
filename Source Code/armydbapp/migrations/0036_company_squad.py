# Generated by Django 2.1.5 on 2019-07-15 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armydbapp', '0035_auto_20190715_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=256)),
                ('company_img', models.ImageField(blank=True, null=True, upload_to='soldiers_imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squad_name', models.CharField(max_length=256)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='armydbapp.Company_commander')),
            ],
        ),
    ]
