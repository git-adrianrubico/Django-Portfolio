# Generated by Django 4.2.6 on 2023-11-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_portfolio_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='filter',
            field=models.CharField(choices=[('filter-project', 'Project'), ('filter-certification', 'Certification'), ('filter-badge', 'Badge')], max_length=50),
        ),
    ]
