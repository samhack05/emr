# Generated by Django 3.0.8 on 2020-07-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0005_auto_20200719_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientvitalinfo',
            name='dateadd',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]