# Generated by Django 3.0.8 on 2020-07-18 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Patient', '0002_billingdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dischargedetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateofbilling', models.DateTimeField(auto_now_add=True)),
                ('Dischargepdf', models.FileField(upload_to='Dischargepapers')),
                ('Dischargename', models.CharField(max_length=25)),
                ('Hospital', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Patient.PatientRecord')),
            ],
        ),
    ]