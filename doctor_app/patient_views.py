from django.shortcuts import render, redirect
from. import models
import datetime
from datetime import date
from django.conf import settings
from django.contrib import messages
    
def patientDashboard(request):
    
    return render(request, 'patient/patient_dashboard.html')



def patient_profile(request):
    if request.session['user_id'] == False:
        return redirect('/')
        
    get_user = models.PatientList.objects.filter(id = request.session['user_id']).first()
    context = {
		'get_user':get_user,
    }
    return render(request, 'patient/patient_profile.html', context)

def getDoctorList(request):
    if request.session['user_id'] == False:
        return redirect('/')

    
    department_list = models.DoctorDepartment.objects.filter(status = True)
    if request.method == "POST":
        department_id = int(request.POST.get('department_id'))
        doctor_lst = models.DoctorList.objects.filter(department_id = department_id)
        
        context = {
			'doctor_lst':doctor_lst,
			'department_list':department_list,
			'department_id': department_id,
		}
        return render(request, 'patient/doctor_list.html', context) 
    else:    
        doctor_lst = models.DoctorList.objects.all()
        context = {
            'doctor_lst':doctor_lst,
            'department_list':department_list,
        }
        return render(request, 'patient/doctor_list.html', context)



def doctor_profile(request,id):
    if request.session['user_id'] == False:
        return redirect('/')
    
    get_user = models.DoctorList.objects.filter(id = id).first()
    context = {
		'get_user':get_user,
	}
    return render(request, 'patient/doctor_profile.html', context)


def my_appiontment(request, id):
	if request.session['user_id'] == False:
		return redirect('/')

	get_doctor = models.DoctorList.objects.get(id = id)
	schedule_list = models.DoctorSchedule.objects.filter(doctor_name_id = id).order_by('id')
	patient_id = request.session['user_id']
	get_patient_remark = models.PatientList.objects.filter(id = patient_id).first()

	today_date = datetime.datetime.now().strftime('%d')
	today_month = datetime.datetime.now().strftime('%m')
	today_year = datetime.datetime.now().strftime('%y') 
	serial_no = str(today_year)+str(today_month)+str(today_date)
	  
	chk_serial = models.AppointmentList.objects.filter(status = True).last()
 
	serial_number_gen = ""
	if not chk_serial:
		serial_number_gen = str(serial_no)+'#'+'01'
	else:
		if len(str(int(chk_serial.id))) < 2: 
			serial_number_gen = str(serial_no)+'#0'+str(int(chk_serial.id+1))
		else:
			serial_number_gen = str(serial_no)+'#'+ str(int(chk_serial.id+1))
   
	if request.method=="POST":
		doctor_id 			= request.POST['doctor_name_id']
		appiontment_date 	= request.POST['appiontment_date']
		appiontment_time 	= request.POST['visiting_hour']
		hospital_name 		= request.POST['hospital_name']
		patient_remarks 	= request.POST['patient_remarks']
		schedule_id 		= request.POST['schedule_name_id']
 
		chk_apointment = models.AppointmentList.objects.filter(schedule_name_id = schedule_id, doctor_name_id = doctor_id, appiontment_date = appiontment_date)
		if chk_apointment: 
			messages.warning(request, 'This schedule time already block for another patient.') 
			return redirect('/patient/doctor/'+str(doctor_id)+'/appiontment/')
		else: 
			models.AppointmentList.objects.create(
				patient_name_id = request.session['user_id'], doctor_name_id = doctor_id, appiontment_date = appiontment_date,
				appiontment_time = appiontment_time, hospital_name = hospital_name, patient_remarks = patient_remarks,
				schedule_name_id = schedule_id, appointment_status = "Pending", serial_number = str(serial_number_gen)
			)
			messages.success(request,'Appiontment Save Successfull, Your serial number is: '+str(serial_number_gen))
			return redirect('/patient/appiontment-list/')
 
	context = {
		'get_doctor':get_doctor,
		'get_patient_remark': get_patient_remark,
		'schedule_list': schedule_list,
	}

	return render(request, 'patient/my_appiontment.html', context)


def appiontment_list(request):
	if request.session['user_id'] == False:
		return redirect('/')

	app_lst = models.AppointmentList.objects.filter(patient_name__id = request.session['user_id']).order_by('-id')

	context = {
		'app_lst':app_lst,
	}
	return render(request, 'patient/appiontment_list.html', context)




def my_prescription(request):
	if request.session['user_id'] == False:
		return redirect('/')

	appiontment_list = models.AppointmentList.objects.filter(patient_name_id = request.session['user_id'])
	context = {
		'appiontment_list':appiontment_list,
	}
	return render(request, 'patient/my_prescription_list.html', context)



def my_test_list(request):
	if request.session['user_id'] == False:
		return redirect('/')
	
	patient_id = request.session['user_id']
	my_test = models.PatientTest.objects.filter(patient_name_id = patient_id)
	
	# my_test = models.MedicalTests.objects.filter(id=patient_id)
	context = {
		'my_test':my_test,
	} 
	return render(request, 'patient/my_test_list.html', context)



 