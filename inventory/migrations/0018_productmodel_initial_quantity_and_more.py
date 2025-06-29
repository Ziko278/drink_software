# Generated by Django 5.0 on 2025-06-17 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_stockinsummarymodel_total_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='initial_quantity',
            field=models.IntegerField(blank=True, default=10, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='initial_quantity_left',
            field=models.IntegerField(blank=True, default=10, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
