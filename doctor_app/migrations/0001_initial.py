# Generated by Django 3.2.18 on 2024-09-18 10:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appiontment_date', models.DateField(blank=True, max_length=100, null=True)),
                ('hospital_name', models.CharField(blank=True, max_length=100, null=True)),
                ('appiontment_time', models.CharField(blank=True, max_length=100, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('appointment_status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed'), ('Reject', 'Reject')], max_length=30)),
                ('patient_remarks', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Appointment List',
                'verbose_name_plural': 'Appointment Patient',
                'db_table': 'appointment_list',
            },
        ),
        migrations.CreateModel(
            name='DoctorDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=100)),
                ('details', models.TextField(blank=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
            ],
            options={
                'verbose_name': 'Doctors Department',
                'verbose_name_plural': 'Department List',
                'db_table': 'doctor_department',
            },
        ),
        migrations.CreateModel(
            name='DoctorList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('user_password', models.CharField(max_length=100, null=True)),
                ('user_phone', models.CharField(max_length=100, null=True)),
                ('user_nid', models.CharField(max_length=100, null=True)),
                ('running_age', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=3)),
                ('fathers_name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('qualification', models.CharField(blank=True, max_length=100)),
                ('working_hour', models.CharField(blank=True, max_length=100)),
                ('weekly_off_day', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('user_images', models.ImageField(upload_to='images/user_images')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctordepartment')),
            ],
            options={
                'verbose_name': 'Doctor List',
                'verbose_name_plural': 'Doctor Information',
                'db_table': 'doctor_list',
            },
        ),
        migrations.CreateModel(
            name='HospitalList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(blank=True, max_length=100, null=True)),
                ('hotline', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('web_link', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Hospital List',
                'verbose_name_plural': 'Hospitals List',
                'db_table': 'hospital_info',
            },
        ),
        migrations.CreateModel(
            name='MedicalTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(blank=True, max_length=100)),
                ('short_name', models.CharField(blank=True, max_length=40)),
                ('test_price', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Medical Test',
                'verbose_name_plural': 'Medical Tests',
                'db_table': 'medical_tests',
            },
        ),
        migrations.CreateModel(
            name='PathologistList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('user_password', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=100)),
                ('working_hour', models.CharField(blank=True, max_length=100)),
                ('weekly_off_day', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('qualification', models.CharField(blank=True, max_length=100)),
                ('spectialist', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('address1', models.TextField(blank=True)),
                ('address2', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctordepartment')),
                ('hospital_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.hospitallist')),
            ],
            options={
                'verbose_name': 'pathologist Info',
                'verbose_name_plural': 'pathologist Information',
                'db_table': 'pathologist_list',
            },
        ),
        migrations.CreateModel(
            name='PatientList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_email', models.EmailField(max_length=100, null=True, unique=True)),
                ('user_password', models.CharField(max_length=100, null=True)),
                ('user_phone', models.CharField(max_length=100, null=True)),
                ('user_nid', models.CharField(max_length=100, null=True)),
                ('running_age', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=3)),
                ('fathers_name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('address1', models.TextField(blank=True, null=True)),
                ('address2', models.TextField(blank=True, null=True)),
                ('patient_images', models.ImageField(upload_to='images/patient_images')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Patient List',
                'verbose_name_plural': 'Patients List',
                'db_table': 'patient_list',
            },
        ),
        migrations.CreateModel(
            name='PharmacyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('user_password', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=100)),
                ('pharmacy_name', models.CharField(blank=True, max_length=100)),
                ('pharmacy_address', models.TextField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('address1', models.TextField(blank=True)),
                ('address2', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Pharmacy Info',
                'verbose_name_plural': 'Pharmacy Information',
                'db_table': 'pharmacy_info',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', ckeditor.fields.RichTextField(blank=True)),
                ('Medicine_name', ckeditor.fields.RichTextField(blank=True)),
                ('serial_number', models.IntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=0)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctorlist')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.patientlist')),
            ],
            options={
                'verbose_name': 'Prescription',
                'verbose_name_plural': 'Prescription for Patient',
                'db_table': 'prescription',
            },
        ),
        migrations.CreateModel(
            name='PatientTestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_report', ckeditor.fields.RichTextField(blank=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.appointmentlist')),
                ('doctor_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctorlist')),
                ('pathologist_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.pathologistlist')),
                ('patient_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.patientlist')),
                ('test_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.medicaltests')),
            ],
            options={
                'verbose_name': 'Patient Test Report',
                'verbose_name_plural': 'Patient Test Reports',
                'db_table': 'patient_test_report',
            },
        ),
        migrations.CreateModel(
            name='PatientTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.appointmentlist')),
                ('doctor_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctorlist')),
                ('patient_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.patientlist')),
                ('test_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.medicaltests')),
            ],
            options={
                'verbose_name': 'Patient Test',
                'verbose_name_plural': 'Patient Test List',
                'db_table': 'patient_tests',
            },
        ),
        migrations.CreateModel(
            name='PatientMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', ckeditor.fields.RichTextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.appointmentlist')),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctorlist')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.patientlist')),
            ],
            options={
                'verbose_name': 'Patient Medicine',
                'verbose_name_plural': 'Patient Medicine Name',
                'db_table': 'patient_medicine',
            },
        ),
        migrations.CreateModel(
            name='DoctorSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_time_in', models.TimeField(blank=True, null=True)),
                ('schedule_time_out', models.TimeField(blank=True, null=True)),
                ('schedule_date', models.DateField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
                ('doctor_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctorlist')),
            ],
            options={
                'verbose_name': 'Doctor Schedule',
                'verbose_name_plural': 'Doctor Schedule List',
                'db_table': 'doctor_schedule',
            },
        ),
        migrations.AddField(
            model_name='doctorlist',
            name='hospital_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.hospitallist'),
        ),
        migrations.AddField(
            model_name='appointmentlist',
            name='doctor_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctorlist'),
        ),
        migrations.AddField(
            model_name='appointmentlist',
            name='patient_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.patientlist'),
        ),
        migrations.AddField(
            model_name='appointmentlist',
            name='schedule_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor_app.doctorschedule'),
        ),
    ]
