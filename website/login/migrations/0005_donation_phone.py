# Generated by Django 3.1.2 on 2020-11-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_donation_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='phone',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]
