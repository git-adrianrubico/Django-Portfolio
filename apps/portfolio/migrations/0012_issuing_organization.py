# Generated by Django 4.2.6 on 2023-11-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_about_photo_alter_personal_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issuing_Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
