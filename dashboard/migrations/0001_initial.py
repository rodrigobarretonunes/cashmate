# Generated by Django 5.2.1 on 2025-06-01 15:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_profiles_avatar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_title', models.CharField(max_length=50)),
                ('transaction_type', models.CharField(max_length=10)),
                ('transaction_date', models.DateField()),
                ('transaction_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_observation', models.TextField(blank=True, max_length=200, null=True)),
                ('transaction_category', models.CharField(max_length=30)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profiles')),
            ],
        ),
    ]
