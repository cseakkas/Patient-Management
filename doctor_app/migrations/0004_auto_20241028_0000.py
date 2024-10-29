# Generated by Django 3.2.18 on 2024-10-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0003_auto_20241027_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pathologistlist',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='pathologistlist',
            old_name='state',
            new_name='fathers_name',
        ),
        migrations.RenameField(
            model_name='pathologistlist',
            old_name='zipcode',
            new_name='mothers_name',
        ),
        migrations.RemoveField(
            model_name='pathologistlist',
            name='address2',
        ),
        migrations.AddField(
            model_name='pathologistlist',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pathologistlist',
            name='running_age',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pathologistlist',
            name='user_nid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pathologistlist',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pathologistlist',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pathologistlist',
            name='user_password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pathologistlist',
            name='user_phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]