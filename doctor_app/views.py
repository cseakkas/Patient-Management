from django.shortcuts import render, redirect
from. import models
from django.conf import settings
from django.contrib import messages

def webHomePage(request):

	return render(request, 'webpage.html')

def loginPage(request):
    if request.method=="POST":
        user_type   = request.POST["user_type"]
        user_email   = request.POST["user_email"]
        user_password   = request.POST["user_password"]
 
        if user_type == "doctor": 
            data = models.DoctorList.objects.filter(user_email = user_email, user_password = user_password).first()
            if data:
                request.session['user_id'] = data.id
                request.session['user_name'] = f"{data.first_name} {data.last_name}" 
                request.session['user_email'] = data.user_email
                request.session['user_type'] = "doctor"
                return redirect('/doctor/dashboard/')
            else: 
                return render(request, 'login.html', {'error': 'Invalid email or password'}) 
        
        elif user_type == "patient": 
            data = models.PatientList.objects.filter(user_email = user_email, user_password = user_password).first()
            if data:
                request.session['user_id'] = data.id
                request.session['user_name'] = f"{data.first_name} {data.last_name}" 
                request.session['user_email'] = data.user_email
                request.session['user_type'] = "patient"
                return redirect('/patient/dashboard/')
            else: 
                return render(request, 'login.html', {'error': 'Invalid email or password'}) 
        else: 
            return render(request, 'login.html', {'error': 'Invalid email or password'}) 

    return render(request, 'login.html')



def log_out(request):
	request.session['user_id'] = False
	request.session['user_name'] = False
	request.session['user_email'] = False
	request.session['user_type'] = False
	return redirect('/login/')


 
def registration_page(request): 
	dept_list = models.DoctorDepartment.objects.filter(status = True).order_by('department_name')
	hospital_list = models.HospitalList.objects.filter(status = True)
	if request.method =="POST":
		user_type = request.POST['usertype']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		father_name = request.POST['father_name']
		mother_name = request.POST['mother_name']
		email = request.POST['email']
		password = request.POST['password']
		phone = request.POST['phone']
		nid = request.POST['nid']
		address = request.POST['address']

		inputCity = request.POST['inputCity'] 
		gender = request.POST['gender']
		running_age = request.POST['running_age']

	 
		user_images = ""
		if bool(request.FILES.get('user_images', False)) == True:
			user_images  = request.FILES['user_images']
			size = 300,330
			im = Image.open(user_images)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(settings.MEDIA_ROOT+"images/user_images/"+ str(user_images), format="JPEG", quality=300)
			user_images = "images/user_images/"+ str(user_images)
		
		if user_type == '1': 
			models.DoctorList.objects.create(
				user_type = user_type,first_name = first_name, last_name = last_name, fathers_name = father_name, mothers_name = mother_name,
				user_email = email, user_password = password, user_phone = phone, user_nid = nid, running_age = running_age, gender = gender,
				city = inputCity, address = address, user_images = user_images,
			 
				designation = request.POST['designation'],  
				qualification = request.POST['qualification'],
				department_id = int(request.POST['department']),
				working_hour = request.POST['working_hour'],
				weekly_off_day = request.POST['weekly_off_day'],  
				hospital_name_id = request.POST['hospital_name'],  
			)
			messages.success(request,'Doctor Registration Successfull')
			return redirect('/registration/')
		
		elif user_type == '3':
			models.PharmacyInfo.objects.create(
				user_type = user_type,first_name = first_name, last_name = last_name, fathers_name = father_name, mothers_name = mother_name,
				user_email = email, user_password = password, user_phone = phone, user_nid = nid, running_age = running_age, gender = gender,
				city = inputCity,  address1 = address, user_images = user_images,
				pharmacy_name = request.POST['pharmacy_name'],
				pharmacy_address = request.POST['pharmacy_address'] 		
			)
			messages.success(request,'pharmacy Registration Successfull')
			return redirect('/registration/')

		elif user_type == '4':
			models.PathologistList.objects.create(
				user_type = user_type,first_name = first_name, last_name = last_name, fathers_name = father_name, mothers_name = mother_name,
				user_email = email, user_password = password, user_phone = phone, user_nid = nid, running_age = running_age, gender = gender,
				city = inputCity, address1 = address, user_images = user_images,
				designation = request.POST['designation'], 
				qualification = request.POST['qualification'],
				department_id = int(request.POST['department']),
				working_hour = request.POST['working_hour'],
				weekly_off_day = request.POST['weekly_off_day'], 				
				hospital_name_id = int(request.POST['hospital_name']) 
			)
			messages.success(request,'pathologist Registration Successfull')
			return redirect('/registration/')
		else:
			models.PatientTest.objects.create(
				user_type = user_type, first_name = first_name, last_name = last_name, 
				fathers_name = father_name, mothers_name = mother_name,
				user_email = email, user_password = password, user_phone = phone, user_nid = nid, 
				running_age = running_age, gender = gender,
				city = inputCity, address1 = address, user_images = user_images
			)
			messages.success(request,'User Registration Successfull')
			return redirect('/registration/')
			
	return render(request, 'registration.html',{'hospital_list': hospital_list, 'dept_list': dept_list})



def doctorDashboard(request):

    return render(request, 'doctor/index.html')



def doctor_profile(request):
	if request.session['user_id'] == False:
		return redirect('/')

	profile = models.DoctorList.objects.get(id = request.session['user_id'])

	context = {
		'profile':profile,
	}
	return render(request, 'doctor/doctor_profile.html', context)



def all_appiontment(request):
    if request.session['user_id'] == False:
        return redirect('/')
        
    doctor_id = request.session['user_id']
    
    if request.method=="POST":
        serial_number = request.POST.get('serial_number', None).strip() 
        appiontment_list = models.AppointmentList.objects.filter(doctor_name_id = doctor_id, serial_number=serial_number)
        context = {
			'serial_number':serial_number, 
			'appiontment_list':appiontment_list,
		}
        return render(request, 'doctor/all_appiontment.html', context)
        
    else:
        appiontment_list = models.AppointmentList.objects.filter(doctor_name_id = doctor_id)
        context={'appiontment_list':appiontment_list,}
        return render(request, 'doctor/all_appiontment.html', context)



def patient_wise_test_write(request, id):
	if request.session['user_id'] == False:
		return redirect('/')

	find_patient = models.AppointmentList.objects.get(id = id)
	test_list = models.MedicalTests.objects.filter(status = True)
	patient_wise_test = models.PatientTest.objects.filter(appointment_id = id, patient_name_id = find_patient.patient_name.id, doctor_name_id = request.session['user_id'])

	if request.method =="POST":
		test_id = request.POST.getlist('test_name') 
		patient_id = int(request.POST['patient_id'])
		appointment_id = int(request.POST['appointment_id']) 
		doctor_id = request.session['user_id']

		for data in test_id:
			models.PatientTest.objects.create(patient_name_id = patient_id, appointment_id = appointment_id, test_name_id = int(data), doctor_name_id = doctor_id)
		
		models.AppointmentList.objects.filter(id = appointment_id, doctor_name_id = doctor_id, patient_name_id = patient_id).update(
			appointment_status = "Processing"
		)
		return redirect('/doctor/patient-list/')
		

	context = {
		'find_patient':find_patient,
		'test_list':test_list, 
		'patient_wise_test': patient_wise_test, 
	}
	return render(request, 'doctor/patient_wise_test_write.html', context)



def patient_list(request):
	if request.session['user_id'] == False:
		return redirect('/')
	
	doctor_id  = request.session['user_id']  
	patient_list = models.AppointmentList.objects.filter(doctor_name_id = doctor_id)
	context ={
		'patient_list':patient_list,
	}

	return render(request, 'doctor/patient_list.html', context)


def doctor_list(request):
    if request.session['user_id'] == False:
        return redirect('/')
        
    doctor_list = models.DoctorList.objects.filter(status=True).exclude(id=request.session['user_id'])
    context ={
		'doctor_list':doctor_list,
	}
    return render(request, 'doctor/doctor_list.html', context)




def patient_wise_write_medicine(request, id):
	if request.session['user_id'] == False:
		return redirect('/')
	
	find_patient  = models.AppointmentList.objects.get(id=id)
	patient_wise_medicine = models.PatientMedicine.objects.filter(appointment_id = id, patient_name_id = find_patient.patient_name.id, doctor_name_id = request.session.get('user_id'))
 
	if request.method =="POST":
		write_medicine = request.POST['write_medicine']
		appointment_id = int(request.POST['appointment_id']) 
		doctor_id = request.session['user_id']

		models.PatientMedicine.objects.create(appointment_id = appointment_id, patient_name_id = find_patient.patient_name.id, medicine_name = write_medicine, doctor_name_id = doctor_id)
		models.AppointmentList.objects.filter(id = id, doctor_name_id = doctor_id, patient_name_id = find_patient.patient_name.id).update(
			appointment_status = "Processing"
		)
		return redirect('/doctor/patient-list/')
        
	context = {
		'find_patient':find_patient,
		'patient_wise_medicine':patient_wise_medicine, 
	}
	return render(request, 'doctor/write_medicine.html', context)


