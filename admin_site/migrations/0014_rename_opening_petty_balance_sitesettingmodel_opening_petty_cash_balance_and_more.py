# Generated by Django 5.0 on 2025-06-17 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0013_activitylogmodel_keywords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesettingmodel',
            old_name='opening_petty_balance',
            new_name='opening_petty_cash_balance',
        ),
        migrations.RenameField(
            model_name='sitesettingmodel',
            old_name='petty_balance',
            new_name='petty_cash_balance',
        ),
    ]
