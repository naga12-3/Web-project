# Generated by Django 3.1.2 on 2020-11-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_userregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]