from django.urls import path
from . import views
from . import patient_views
urlpatterns = [
    path('', views.webHomePage, name="webHomePage"), 
    path('login/', views.loginPage, name="loginPage"), 
    path('registration/', views.registration_page),
    path('logout/', views.log_out),  
    path('doctor/dashboard/', views.doctorDashboard, name="doctorDashboard"),

    ############# Doctor Urls  #################
    path('doctor/profile/', views.doctor_profile), 
    path('doctor/appiontment-list/', views.all_appiontment), 
    path('doctor/patient/<int:id>/write-test/', views.patient_wise_test_write),
    path('doctor/patient/<int:id>/write-medicine/', views.patient_wise_write_medicine),
    path('doctor/patient-list/', views.patient_list),
    path('doctor-list/', views.doctor_list),

    # path('doctor/find-patient/', views.find_a_patient),
    # path('doctor/patient-list/', views.patient_list),
    # path('doctor/all-patient/', views.all_patient),
    # path('doctor-list/', views.doctor_list),
    # path('test-list/', views.test_list),
    # path('prescription/', views.prescription),
    # path('patient-test/', views.patient_test),
    # path('doctor/patient-test-report/', views.doctor_patient_test_report),
    # path('patient-medicine/', views.patient_medicine),
    # path('patient/<int:id>/write-test/', views.patient_wise_test_write),
    # path('patient/<int:id>/write-medicine/', views.patient_wise_write_medicine),
    # path('patient/<int:appointment_id>/view-prescription/', views.patient_wise_prescription),
    # path('patient/<int:appointment_id>/patient-prescription-view/', views.patient_prescription_list),
 
    # path('doctor/patient/<int:id>/view-test-report/', views.view_test_report_by_doctor),
    # path('doctor/patient/<int:id>/view-medicine/', views.view_patient_medicine_by_doctor),


    path('patient/dashboard/', patient_views.patientDashboard, name="patientDashboard"),
    path('patient/profile/', patient_views.patient_profile),
    path('patient/doctor-list/', patient_views.getDoctorList), 
    path('patient/doctor/<int:id>/profile/', patient_views.doctor_profile), 
    path('patient/doctor/<int:id>/appiontment/', patient_views.my_appiontment), 
    path('patient/appiontment-list/', patient_views.appiontment_list), 
    path('patient/my-prescription-list/', patient_views.my_prescription),
    path('patient/my-test-list/', patient_views.my_test_list),

]
