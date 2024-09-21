# Generated by Django 3.2.18 on 2024-09-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorlist',
            name='spectialist',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='doctorlist',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='doctorlist',
            name='qualification',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]