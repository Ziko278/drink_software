# Generated by Django 5.0 on 2025-06-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_alter_salemodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salemodel',
            name='delivery_status',
            field=models.CharField(choices=[('self', 'Self Collection'), ('driver', 'Delivered by Driver')], max_length=20),
        ),
    ]
