# Generated by Django 5.0 on 2025-06-19 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0014_rename_opening_petty_balance_sitesettingmodel_opening_petty_cash_balance_and_more'),
        ('human_resource', '0004_staffmodel_crate_target_for_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitylogmodel',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='human_resource.staffmodel'),
        ),
    ]
