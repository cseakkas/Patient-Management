from django.shortcuts import render, redirect
from. import models

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
	return redirect('/')



def doctorDashboard(request):

    return render(request, 'doctor/index.html')



def doctor_profile(request):
	if request.session['user_email'] == False:
		return redirect('/')

	profile = models.DoctorList.objects.get(id = request.session['user_id'])

	context = {
		'profile':profile,
	}
	return render(request, 'doctor/doctor_profile.html', context)






