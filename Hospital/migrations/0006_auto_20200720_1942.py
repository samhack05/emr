# Generated by Django 3.0.8 on 2020-07-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_auto_20200719_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalcircle',
            name='otp',
            field=models.CharField(default=573965, max_length=20),
        ),
    ]
