# Generated by Django 5.1.4 on 2025-01-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
