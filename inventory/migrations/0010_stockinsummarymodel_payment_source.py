# Generated by Django 5.0 on 2025-06-16 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_productmodel_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockinsummarymodel',
            name='payment_source',
            field=models.CharField(choices=[('cash', 'CASH'), ('bank', 'BANK')], default='bank', max_length=10),
            preserve_default=False,
        ),
    ]
