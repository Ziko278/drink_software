# Generated by Django 5.0 on 2025-06-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettingmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2000-12-12'),
            preserve_default=False,
        ),
    ]
