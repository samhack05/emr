# Generated by Django 3.0.8 on 2020-07-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0010_auto_20200720_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalcircle',
            name='otp',
            field=models.CharField(default=150046, max_length=20),
        ),
    ]