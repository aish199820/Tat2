# Generated by Django 4.1.4 on 2023-01-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToursApp', '0005_destinationmodel_dinfo_destinationmodel_dphoto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]