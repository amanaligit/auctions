# Generated by Django 3.1.4 on 2020-12-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20201202_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.Listing'),
        ),
    ]
