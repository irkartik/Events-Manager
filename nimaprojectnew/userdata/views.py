from django.shortcuts import render, redirect
from .models import Eligibility, Appointment, AppliedUser
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets, generics
from .serializers import AppointmentSerializer, EligibilitySerializer, AppliedUserSerializer



class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Appointments to be viewed or edited.
    """
    queryset = Appointment.objects.all().order_by('-created_date')
    serializer_class = AppointmentSerializer

class EligibilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Eligibility form data to be viewed or edited.
    """
    queryset = Eligibility.objects.all().order_by('-created_date')
    serializer_class = EligibilitySerializer

class AppliedUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Eligibility form data to be viewed or edited.
    """
    queryset = AppliedUser.objects.all().order_by('-created_date')
    serializer_class = AppliedUserSerializer

class AppointmentIndivisual(generics.ListAPIView):
	serializer_class = AppointmentSerializer

	def get_queryset(self):
		appointment_id = self.kwargs['appointment_id']
		return Appointment.objects.filter(id=appointment_id)

class AppliedUserIndivisual(generics.ListAPIView):
	serializer_class = AppliedUserSerializer

	def get_queryset(self):
		applieduser_id = self.kwargs['applieduser_id']
		return AppliedUser.objects.filter(id=applieduser_id)

class EligibilityIndivisual(generics.ListAPIView):
	serializer_class = EligibilitySerializer

	def get_queryset(self):
		eligibility_id = self.kwargs['eligibility_id']
		return Eligibility.objects.filter(id=eligibility_id)

@login_required(login_url="/login")
def show_appointments(request):
	users = Appointment.objects.all().order_by('-created_date')
	print(users)
	context = {
		'appointments' : users,
	}

	return render(request, 'userdata/show_appointments.html', context)

def create_appointment(request):
	if request.method=="POST":
		full_name = request.POST.get('full_name')
		address = request.POST.get('address')
		telephone_no = request.POST.get('telephone_no')
		mobile_no = request.POST.get('mobile_no')
		email = request.POST.get('email')
		purpose_of_visit = request.POST.get('purpose_of_visit')
		evidence_of_id = request.POST.get('evidence_of_id')
		evidence_of_id_number = request.POST.get('evidence_of_id_number')
		appointment = request.POST.get('appointment')
		date = request.POST.get('date')
		time = request.POST.get('time')
		message = request.POST.get('message')

		temp = Appointment.objects.create(full_name = full_name, address = address, telephone_no = telephone_no, mobile_no = mobile_no, email = email, purpose_of_visit = purpose_of_visit, evidence_of_id = evidence_of_id, evidence_of_id_number = evidence_of_id_number, appointment = appointment, date = date, time = time, message = message)
		temp.save()

		return HttpResponse('Thank you')
	else:
		context = {}
		return render(request, 'userdata/create_appointment_form.html', context)


def create_check_eligibility(request):
	if request.method=="POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		qualification = request.POST.get('qualification')
		ielts = request.POST.get('ielts')
		toefl = request.POST.get('toefl')
		sat = request.POST.get('sat')
		gre = request.POST.get('gre')
		gmat = request.POST.get('gmat')
		pte = request.POST.get('pte')
		priority_country = request.POST.get('priority_country')
		remarks = request.POST.get('remarks')
		
		temp = Eligibility.objects.create(name = name, email = email, address = address, phone = phone, qualification = qualification, ielts = ielts, toefl = toefl, sat = sat, gre = gre, gmat = gmat, pte = pte, priority_country = priority_country, remarks = remarks)
		temp.save()

		return HttpResponse('Thank you')
	else:
		context = {}
		return render(request, 'userdata/create_check_eligibility.html', context)


@login_required(login_url="/login")
def show_eligibility(request):
	users = Eligibility.objects.all().order_by('-created_date')
	print(users)
	context = {
		'eligibilities' : users,
	}

	return render(request, 'userdata/show_eligibility.html', context)

@login_required(login_url='/login')
def full_eligibility(request, eligibility_id):
	user = Eligibility.objects.get(id=eligibility_id)

	context = {
		'user': user,
	}
	return render(request, 'userdata/show_indivisual_eligibility.html', context)

@login_required(login_url="/login")
def show_applied_users(request):
	users = AppliedUser.objects.all().order_by('-created_date')
	print(users)
	context = {
		'appliedusers' : users,
	}

	return render(request, 'userdata/show_applied_users.html', context)

@login_required(login_url="/login")
def show_full_profile(request, user_id):
	user = AppliedUser.objects.get(id=user_id)
	context = {
		'user' : user,
	}
	return render(request, 'userdata/show_profile.html', context)
	
def apply_now(request):
	if request.method == "POST":
		year = request.POST.get('year')
		intake = request.POST.get('intake')
		course = request.POST.get('course')
		permanent_country = request.POST.get('permanent_country')
		title = request.POST.get('title')
		last_name = request.POST.get('last_name')
		middle_name = request.POST.get('middle_name')
		first_name = request.POST.get('first_name')
		date_of_birth = request.POST.get('date_of_birth')
		place_of_birth = request.POST.get('place_of_birth')
		sex = request.POST.get('sex')
		nationality = request.POST.get('nationality')
		marital_status = request.POST.get('marital_status')
		citizenship_number = request.POST.get('citizenship_number')
		passport_number = request.POST.get('passport_number')
		date_of_issue = request.POST.get('date_of_issue')
		date_of_expiry = request.POST.get('date_of_expiry')
		place_of_issue = request.POST.get('place_of_issue')
		street_name_number = request.POST.get('street_name_number')
		city = request.POST.get('city')
		state = request.POST.get('state')
		country = request.POST.get('country')
		phone = request.POST.get('phone')
		mobile = request.POST.get('mobile')
		email = request.POST.get('email')
		is_permanent = request.POST.get('is_permanent')
		school_name = request.POST.get('school_name')
		school_city = request.POST.get('school_city')
		school_state = request.POST.get('school_state')
		school_country = request.POST.get('school_country')
		school_qualification_obtained = request.POST.get('school_qualification_obtained')
		school_marks_obtained = request.POST.get('school_marks_obtained')
		school_date_of_completion = request.POST.get('school_date_of_completion')
		high_school_name = request.POST.get('high_school_name')
		high_school_city = request.POST.get('high_school_city')
		high_school_state = request.POST.get('high_school_state')
		high_school_country = request.POST.get('high_school_country')
		high_school_qualification_obtained = request.POST.get('high_school_qualification_obtained')
		high_school_marks_obtained = request.POST.get('high_school_marks_obtained')
		high_school_date_of_completion = request.POST.get('high_school_date_of_completion')
		undergrad_university = request.POST.get('undergrad_university')
		undergrad_city = request.POST.get('undergrad_city')
		undergrad_state = request.POST.get('undergrad_state')
		undergrad_country = request.POST.get('undergrad_country')
		undergrad_degree_obtained = request.POST.get('undergrad_degree_obtained')
		undergrad_major_subject = request.POST.get('undergrad_major_subject')
		undergrad_marks_obtained = request.POST.get('undergrad_marks_obtained')
		undergrad_date_of_completion = request.POST.get('undergrad_date_of_completion')
		graduate_university = request.POST.get('graduate_university')
		graduate_city = request.POST.get('graduate_city')
		graduate_state = request.POST.get('graduate_state')
		graduate_country = request.POST.get('graduate_country')
		graduate_degree_obtained = request.POST.get('graduate_degree_obtained')
		graduate_major_subject = request.POST.get('graduate_major_subject')
		graduate_marks_obtained = request.POST.get('graduate_marks_obtained')
		graduate_date_of_completion = request.POST.get('graduate_date_of_completion')
		ielts = request.POST.get('ielts')
		toefl = request.POST.get('toefl')
		sat = request.POST.get('sat')
		gre = request.POST.get('gre')
		gmat = request.POST.get('gmat')
		pte = request.POST.get('pte')
		employment_current_employer = request.POST.get('employment_current_employer')
		field_of_activity = request.POST.get('field_of_activity')
		position = request.POST.get('position')
		start_date = request.POST.get('start_date')
		department = request.POST.get('department')
		employment_type = request.POST.get('employment_type')
		responsibilites = request.POST.get('responsibilites')
		previous_employer = request.POST.get('previous_employer')
		previous_location = request.POST.get('previous_location')
		previous_job_title = request.POST.get('previous_job_title')
		previous_start_date = request.POST.get('previous_start_date')
		previous_end_date = request.POST.get('previous_end_date')
		previous_employment_type = request.POST.get('previous_employment_type')
		question1 = request.POST.get('question1')
		question2 = request.POST.get('question2')
		question3 = request.POST.get('question3')
		question4 = request.POST.get('question4')
		question5 = request.POST.get('question5')
		question6 = request.POST.get('question6')
		question7 = request.POST.get('question7')
		question8 = request.POST.get('question8')
		statement_of_purpose = request.POST.get('statement_of_purpose')
		photograph = request.FILES['photograph']
		resume = request.FILES['resume']
		passport_copy = request.FILES['passport_copy']
		citizenship_copy = request.FILES['citizenship_copy']
		school_education_certificate = request.FILES['school_education_certificate']
		high_school_certificate = request.FILES['high_school_certificate']
		undergrad_certificate = request.FILES['undergrad_certificate']
		graduate_certificate = request.FILES['graduate_certificate']
		test = request.FILES['test']
		signature_name = request.POST.get('signature_name')
		date_of_signature = request.POST.get('date_of_signature')

		certification = request.POST.get('certification')

		if certification == 'on':
		  certification = True
		else:
		  certification = False

		if is_permanent == 'Yes':
		  is_permanent = True
		else:
		  is_permanent=False


		temp = AppliedUser.objects.create(year = year, intake = intake, course = course, permanent_country = permanent_country, title = title, last_name = last_name, middle_name = middle_name, first_name = first_name, date_of_birth = date_of_birth, place_of_birth = place_of_birth, sex = sex, nationality = nationality, marital_status = marital_status, citizenship_number = citizenship_number, passport_number = passport_number, date_of_issue = date_of_issue, date_of_expiry = date_of_expiry, place_of_issue = place_of_issue, street_name_number = street_name_number, city = city, state = state, country = country, phone = phone, mobile = mobile, email = email, is_permanent = is_permanent, school_name = school_name, school_city = school_city, school_state = school_state, school_country = school_country, school_qualification_obtained = school_qualification_obtained, school_marks_obtained = school_marks_obtained, school_date_of_completion = school_date_of_completion, high_school_name = high_school_name, high_school_city = high_school_city, high_school_state = high_school_state, high_school_country = high_school_country, high_school_qualification_obtained = high_school_qualification_obtained, high_school_marks_obtained = high_school_marks_obtained, high_school_date_of_completion = high_school_date_of_completion, undergrad_university = undergrad_university, undergrad_city = undergrad_city, undergrad_state = undergrad_state, undergrad_country = undergrad_country, undergrad_degree_obtained = undergrad_degree_obtained, undergrad_major_subject = undergrad_major_subject, undergrad_marks_obtained = undergrad_marks_obtained, undergrad_date_of_completion = undergrad_date_of_completion, graduate_university = graduate_university, graduate_city = graduate_city, graduate_state = graduate_state, graduate_country = graduate_country, graduate_degree_obtained = graduate_degree_obtained, graduate_major_subject = graduate_major_subject, graduate_marks_obtained = graduate_marks_obtained, graduate_date_of_completion = graduate_date_of_completion, ielts = ielts, toefl = toefl, sat = sat, gre = gre, gmat = gmat, pte = pte, employment_current_employer = employment_current_employer, field_of_activity = field_of_activity, position = position, start_date = start_date, department = department, employment_type = employment_type, responsibilites = responsibilites, previous_employer = previous_employer, previous_location = previous_location, previous_job_title = previous_job_title, previous_start_date = previous_start_date, previous_end_date = previous_end_date, previous_employment_type = previous_employment_type, question1 = question1, question2 = question2, question3 = question3, question4 = question4, question5 = question5, question6 = question6, question7 = question7, question8 = question8, statement_of_purpose = statement_of_purpose, photograph = photograph, resume = resume, passport_copy = passport_copy, citizenship_copy = citizenship_copy, school_education_certificate = school_education_certificate, high_school_certificate = high_school_certificate, undergrad_certificate = undergrad_certificate, graduate_certificate = graduate_certificate, test = test, signature_name = signature_name, date_of_signature = date_of_signature, certification=certification)

		temp.save()
		return HttpResponse('Thank You')
	else:
		return render(request, 'userdata/apply_now.html')

@login_required(login_url="/login")
def full_appointment(request, appointment_id):
	temp = Appointment.objects.get(id=appointment_id)
	context = {
		'appointment': temp
	}
	return render(request, 'userdata/full_appointment.html', context)








