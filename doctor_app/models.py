from django.db import models
from datetime import datetime
import os
from ckeditor.fields import RichTextField
 
class HospitalList(models.Model):
    hospital_name        = models.CharField(max_length=100, blank=True, null=True)
    hotline              = models.CharField(max_length=100, blank=True, null=True)
    address              = models.TextField( blank=True, null=True)
    web_link             = models.CharField(max_length=100, blank=True, null=True) 
    status               = models.BooleanField(default=True)

    def __int__(self):
        return self.hospital_name
 
    class Meta:
        db_table = 'hospital_info'
        verbose_name = 'Hospital List'
        verbose_name_plural = 'Hospitals List'
  
class DoctorDepartment(models.Model): 
    department_name     = models.CharField(max_length=100, blank=True)   
    details             = models.TextField(blank=True)
    create_date         = models.DateField(auto_now_add=True)
    status              = models.BooleanField(default=1)

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = 'doctor_department'
        verbose_name = 'Doctors Department'
        verbose_name_plural = 'Department List'
 

class PatientList(models.Model): 
    first_name          = models.CharField(max_length=100, blank=True, null=True)
    last_name           = models.CharField(max_length=100, blank=True, null=True)
    user_email          = models.EmailField(max_length=100, unique = True, null=True)
    user_password       = models.CharField(max_length=100, null=True)
    user_phone          = models.CharField(max_length=100, null=True)
    user_nid            = models.CharField(max_length=100, null=True)
    running_age         = models.CharField(max_length=100, null=True)
    gender_type = (
        ('1',  'Male'),
        ('2',  'Female'),
    )
    gender           = models.CharField(max_length=3, choices=gender_type)
    fathers_name        = models.CharField(max_length=100)
    mothers_name        = models.CharField(max_length=100)
    city                = models.CharField(max_length=100)
    state               = models.CharField(max_length=100)
    zipcode             = models.CharField(max_length=100)
    address1            = models.TextField(blank=True, null=True)
    address2            = models.TextField(blank=True, null=True) 
    patient_images         = models.ImageField(upload_to='images/patient_images')
    status              = models.BooleanField(default=True)
    created         = models.DateField(auto_now_add=True, null=True) 
    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "patient_list"
        verbose_name = 'Patient List'
        verbose_name_plural = 'Patients List'

class DoctorList(models.Model): 
    first_name          = models.CharField(max_length=100, blank=True, null=True)
    last_name           = models.CharField(max_length=100, blank=True, null=True)
    user_email          = models.EmailField(max_length=100, unique = True)
    user_password       = models.CharField(max_length=100, null=True)
    user_phone          = models.CharField(max_length=100, null=True)
    user_nid            = models.CharField(max_length=100, null=True)
    running_age         = models.CharField(max_length=100, null=True)
    gender_type = (
        ('Male',  'Male'),
        ('Female',  'Female'),
    )
    gender              = models.CharField(max_length=10, choices=gender_type)
    fathers_name        = models.CharField(max_length=100)
    mothers_name        = models.CharField(max_length=100)
    designation         = models.CharField(max_length=100,blank=True)
    qualification       = models.CharField(max_length=255,blank=True)
    spectialist         = models.CharField(max_length=255,blank=True)
    department          = models.ForeignKey(DoctorDepartment, on_delete=models.DO_NOTHING, blank=True, null=True)
    hospital_name       = models.ForeignKey(HospitalList, on_delete=models.DO_NOTHING, blank=True, null=True)
    working_hour        = models.CharField(max_length=100,blank=True)
    weekly_off_day      = models.CharField(max_length=100,blank=True) 
    city                = models.CharField(max_length=100)
    state               = models.CharField(max_length=100)
    zipcode             = models.CharField(max_length=100)
    address            = models.TextField(blank=True)
    user_images         = models.ImageField(upload_to='images/user_images')
    upload_date         = models.DateField(auto_now_add=True) 
    status              = models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "doctor_list"
        verbose_name = 'Doctor List'
        verbose_name_plural = 'Doctor Information'
 
class DoctorSchedule(models.Model): 
    doctor_name           = models.ForeignKey(DoctorList, on_delete=models.DO_NOTHING, blank=True, null=True) 
    schedule_time_in      = models.TimeField( blank=True, null=True)
    schedule_time_out     = models.TimeField( blank=True, null=True)
    schedule_date         = models.DateField(auto_now_add=False)
    create_date           = models.DateField(auto_now_add=True)
    status                = models.BooleanField(default=1)

    def __int__(self):
        return self.doctor_name

    class Meta:
        db_table = "doctor_schedule"
        verbose_name = 'Doctor Schedule'
        verbose_name_plural = 'Doctor Schedule List'

class AppointmentList(models.Model):
    patient_name         = models.ForeignKey(PatientList, on_delete=models.DO_NOTHING, blank=True, null=True)
    doctor_name          = models.ForeignKey(DoctorList, on_delete=models.DO_NOTHING, blank=True, null=True)
    schedule_name        = models.ForeignKey(DoctorSchedule, on_delete=models.DO_NOTHING, blank=True, null=True)
    appiontment_date     = models.DateField(max_length=100, blank=True, null=True)
    hospital_name        = models.CharField(max_length=100, blank=True, null=True)
    appiontment_time     = models.CharField(max_length=100, blank=True, null=True)
    serial_number        = models.CharField(max_length=100, blank=True, null=True)
    app_status = (
        ('Pending',  'Pending'),
        ('Processing',  'Processing'),
        ('Completed',  'Completed'),
        ('Reject',  'Reject'),
    )
    appointment_status   = models.CharField(max_length=30, choices=app_status)
    patient_remarks      = models.TextField(blank=True, null=True)
    status               = models.BooleanField(default=True)

    def __int__(self):
        return self.doctor_name

    class Meta:
        db_table = "appointment_list"
        verbose_name = 'Appointment List'
        verbose_name_plural = 'Appointment Patient'

class MedicalTests(models.Model):
    test_name        = models.CharField(max_length=100, blank=True)
    short_name       = models.CharField(max_length=40, blank=True)
    test_price       = models.IntegerField(default=0)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.test_name

    class Meta:
        db_table = "medical_tests"
        verbose_name = 'Medical Test'
        verbose_name_plural = 'Medical Tests'


class Prescription(models.Model):
    patient_name        = models.ForeignKey(PatientList, on_delete=models.DO_NOTHING)
    doctor_name         = models.ForeignKey(DoctorList, on_delete=models.DO_NOTHING)
    test_name           = RichTextField(blank=True)
    Medicine_name       = RichTextField(blank=True)
    serial_number       = models.IntegerField(default=0)
    created         = models.DateField(auto_now_add=True)
    status              = models.BooleanField(default=0)

    def __str__(self):
        return self.test_name

    class Meta:
        db_table='prescription'
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescription for Patient'

class PatientTest(models.Model):
    patient_name        = models.ForeignKey(PatientList, on_delete=models.DO_NOTHING, blank=True, null=True)
    appointment         = models.ForeignKey(AppointmentList, on_delete=models.DO_NOTHING, blank=True, null=True) 
    doctor_name         = models.ForeignKey(DoctorList, on_delete=models.DO_NOTHING, blank=True, null=True)
    test_name           = models.ForeignKey(MedicalTests, on_delete=models.DO_NOTHING, blank=True, null=True)
    created        = models.DateField(auto_now_add=True)
    status              = models.BooleanField(default=1)

    def __str__(self):
        return self.test_name

    class Meta:
        db_table='patient_tests'
        verbose_name = 'Patient Test'
        verbose_name_plural = 'Patient Test List'

class PatientMedicine(models.Model):
    patient_name        = models.ForeignKey(PatientList, on_delete=models.DO_NOTHING)
    appointment         = models.ForeignKey(AppointmentList, on_delete=models.DO_NOTHING, blank=True, null=True)
    doctor_name         = models.ForeignKey(DoctorList, on_delete=models.DO_NOTHING)
    medicine_name       = RichTextField(blank=True)
    created         = models.DateField(auto_now_add=True)
    status              = models.BooleanField(default=1)

    def __str__(self):
        return self.medicine_name

    class Meta:
        db_table='patient_medicine'
        verbose_name = 'Patient Medicine'
        verbose_name_plural = 'Patient Medicine Name'


# class PharmacyPrescription(models.Model):
#     patient_name        = models.ForeignKey(PatientList, on_delete=models.DO_NOTHING)
#     doctor_name         = models.ForeignKey(DoctorList, on_delete=models.DO_NOTHING)
#     test_name           = models.CharField(max_length=40, blank=True)
#     serial_number       = models.IntegerField(default=0)
#     details             = models.TextField( blank=True)
#     create_date         = models.DateField(auto_now_add=True)
#     status              = models.BooleanField(default=0)

#     def __str__(self):
#         return self.test_name

#     class Meta:
#         db_table='pharmacy_prescription'
#         verbose_name = 'Prescription'
#         verbose_name_plural = 'Pharmacy Prescription'


##############################   Pharmacy      #############################

class PharmacyInfo(models.Model): 
    first_name          = models.CharField(max_length=100, blank=True, null=True)
    last_name           = models.CharField(max_length=100, blank=True, null=True)
    user_email          = models.EmailField(max_length=100, unique = True)
    user_password       = models.CharField(max_length=100, null=True)
    user_phone          = models.CharField(max_length=100, null=True)
    user_nid            = models.CharField(max_length=100, null=True)
    running_age         = models.CharField(max_length=100, null=True)
    gender_type = (
        ('Male',  'Male'),
        ('Female',  'Female'),
    )
    gender              = models.CharField(max_length=10, choices=gender_type)
    fathers_name        = models.CharField(max_length=100)
    mothers_name        = models.CharField(max_length=100)
 
    pharmacy_name       = models.CharField(max_length=100,blank=True)
    pharmacy_address    = models.TextField(max_length=100,blank=True)
    city                = models.CharField(max_length=100) 
    address             = models.TextField(blank=True)
    created             = models.DateField(auto_now_add=True) 
    status              = models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "pharmacy_info"
        verbose_name = 'Pharmacy Info'
        verbose_name_plural = 'Pharmacy Information'

##############################   pathologist  #############################

class PathologistList(models.Model): 
    first_name          = models.CharField(max_length=100, blank=True, null=True)
    last_name           = models.CharField(max_length=100, blank=True, null=True)
    user_email          = models.EmailField(max_length=100, unique = True)
    user_password       = models.CharField(max_length=100, null=True)
    user_phone          = models.CharField(max_length=100, null=True)
    user_nid            = models.CharField(max_length=100, null=True)
    running_age         = models.CharField(max_length=100, null=True)
    gender_type = (
        ('Male',  'Male'),
        ('Female',  'Female'),
    )
    gender              = models.CharField(max_length=10, choices=gender_type)
    fathers_name        = models.CharField(max_length=100)
    mothers_name        = models.CharField(max_length=100)
    
    department          = models.ForeignKey(DoctorDepartment, on_delete=models.DO_NOTHING, blank=True, null=True)
    hospital_name       = models.ForeignKey(HospitalList, on_delete=models.DO_NOTHING, blank=True, null=True)
    working_hour        = models.CharField(max_length=100,blank=True)
    weekly_off_day      = models.CharField(max_length=100,blank=True)
    designation         = models.CharField(max_length=100,blank=True)
    qualification       = models.CharField(max_length=100,blank=True)
    spectialist         = models.CharField(max_length=100,blank=True)  
    city                = models.CharField(max_length=100)
    address             = models.TextField(blank=True)
    created             = models.DateField(auto_now_add=True) 
    status              = models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "pathologist_list"
        verbose_name = 'pathologist Info'
        verbose_name_plural = 'pathologist Information'



class PatientTestReport(models.Model):
    patient_name        = models.ForeignKey(PatientList, on_delete=models.DO_NOTHING, blank=True, null=True)
    doctor_name         = models.ForeignKey(DoctorList, on_delete=models.DO_NOTHING, blank=True, null=True)
    pathologist_name    = models.ForeignKey(PathologistList, on_delete=models.DO_NOTHING, blank=True, null=True)
    test_name           = models.ForeignKey(MedicalTests, on_delete=models.DO_NOTHING, blank=True, null=True)
    appointment         = models.ForeignKey(AppointmentList, on_delete=models.DO_NOTHING, blank=True, null=True)
    test_report         = RichTextField( blank=True)
    create_date         = models.DateField(auto_now_add=True)
    status              = models.BooleanField(default=1)

    def __str__(self):
        return self.test_name

    class Meta:
        db_table = "patient_test_report"
        verbose_name = 'Patient Test Report'
        verbose_name_plural = 'Patient Test Reports'
