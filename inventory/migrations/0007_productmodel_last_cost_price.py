# Generated by Django 5.0 on 2025-06-15 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_stockoutmodel_stock_out_empty'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='last_cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
