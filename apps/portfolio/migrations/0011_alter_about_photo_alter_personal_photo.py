# Generated by Django 4.2.6 on 2023-11-11 09:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_portfolio_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_pic/about'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_pic/main'),
        ),
    ]
