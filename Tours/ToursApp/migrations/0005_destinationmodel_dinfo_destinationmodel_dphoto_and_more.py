# Generated by Django 4.1.4 on 2023-01-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursApp', '0004_destinationmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationmodel',
            name='dinfo',
            field=models.TextField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='destinationmodel',
            name='dphoto',
            field=models.ImageField(blank=True, upload_to='dphotos/'),
        ),
        migrations.AddField(
            model_name='packagemodel',
            name='numdays',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
