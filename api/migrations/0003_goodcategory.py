# Generated by Django 5.1.4 on 2025-01-11 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customer_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.goodcategory')),
            ],
        ),
    ]
