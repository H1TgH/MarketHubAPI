# Generated by Django 5.1.4 on 2025-01-13 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_otp_user_delete_customer_delete_verificationcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.good')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
