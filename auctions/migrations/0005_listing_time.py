# Generated by Django 3.1.4 on 2020-12-01 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201201_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
