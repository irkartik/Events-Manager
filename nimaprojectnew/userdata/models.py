from django.db import models
from core.models import Branch

# Create your models here.

class Eligibility(models.Model):
	name = models.CharField(max_length=1000)
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	email = models.EmailField()
	address = models.TextField()
	phone = models.CharField(max_length=1000)
	qualification = models.CharField(max_length=100)
	ielts = models.CharField(max_length=1000, blank=True, null=True)
	toefl = models.CharField(max_length=1000, blank=True, null=True)
	sat = models.CharField(max_length=1000, blank=True, null=True)
	gre = models.CharField(max_length=1000, blank=True, null=True)
	gmat = models.CharField(max_length=1000, blank=True, null=True)
	pte = models.CharField(max_length=1000, blank=True, null=True)
	priority_country = models.CharField(max_length=100, blank=True, null=True)
	remarks = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Appointment(models.Model):
	full_name = models.CharField(max_length=1000)
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	address = models.TextField()
	telephone_no = models.CharField(max_length=100)
	mobile_no = models.CharField(max_length=100)
	email = models.EmailField()
	purpose_of_visit = models.CharField(max_length=100)
	evidence_of_id = models.CharField(max_length=100)
	evidence_of_id_number = models.CharField(max_length=100)
	appointment = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	time = models.CharField(max_length=100)
	message = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.full_name

class AppliedUser(models.Model):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True)
	year = models.CharField(max_length=4, blank=True, null=True)
	intake = models.CharField(max_length=50,blank=True, null=True)
	course = models.CharField(max_length=100,blank=True, null=True)
	permanent_country = models.CharField(max_length=50,blank=True, null=True)
	title = models.CharField(max_length=5,blank=True, null=True)
	last_name = models.CharField(max_length=10,blank=True, null=True)
	middle_name = models.CharField(max_length=10, blank=True, null=True)
	first_name = models.CharField(max_length=10,blank=True, null=True)
	date_of_birth = models.CharField(max_length=10,blank=True, null=True)
	place_of_birth = models.CharField(max_length=100,blank=True, null=True)
	sex = models.CharField(max_length=10,blank=True, null=True)
	nationality = models.CharField(max_length=50,blank=True, null=True)
	marital_status = models.CharField(max_length=50,blank=True, null=True)
	citizenship_number = models.CharField(max_length=100, blank=True, null=True)
	passport_number = models.CharField(max_length=100, null=True, blank=True)
	date_of_issue = models.CharField(max_length=100, null=True, blank=True)
	date_of_expiry = models.CharField(max_length=100, null=True, blank=True)
	place_of_issue = models.CharField(max_length=100, blank=True, null=True)
	
	street_name_number = models.CharField(max_length=1000, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=100, null=True, blank=True)
	mobile = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	is_permanent = models.BooleanField(max_length=10)
	
	school_name = models.CharField(max_length=1000, null=True, blank=True)
	school_city = models.CharField(max_length=100, null=True, blank=True)
	school_state = models.CharField(max_length=100, null=True, blank=True)
	school_country = models.CharField(max_length=100, null=True, blank=True)
	school_qualification_obtained = models.CharField(max_length=1000, null=True, blank=True)
	school_marks_obtained = models.CharField(max_length=100, null=True, blank=True)
	school_date_of_completion = models.CharField(max_length=100, null=True, blank=True)

	high_school_name = models.CharField(max_length=1000, null=True, blank=True)
	high_school_city = models.CharField(max_length=100, null=True, blank=True)
	high_school_state = models.CharField(max_length=100, null=True, blank=True)
	high_school_country = models.CharField(max_length=100, null=True, blank=True)
	high_school_qualification_obtained = models.CharField(max_length=1000, null=True, blank=True)
	high_school_marks_obtained = models.CharField(max_length=100, null=True, blank=True)
	high_school_date_of_completion = models.CharField(max_length=100, null=True, blank=True)

	undergrad_university = models.CharField(max_length=1000, null=True, blank=True)
	undergrad_city = models.CharField(max_length=100, null=True, blank=True)
	undergrad_state = models.CharField(max_length=100, null=True, blank=True)
	undergrad_country = models.CharField(max_length=100, null=True, blank=True)
	undergrad_degree_obtained = models.CharField(max_length=1000, null=True, blank=True)
	undergrad_major_subject = models.CharField(max_length=100, null=True, blank=False)
	undergrad_marks_obtained = models.CharField(max_length=100, null=True, blank=True)
	undergrad_date_of_completion = models.CharField(max_length=100, null=True, blank=True)

	graduate_university = models.CharField(max_length=1000, null=True, blank=True)
	graduate_city = models.CharField(max_length=100, null=True, blank=True)
	graduate_state = models.CharField(max_length=100, null=True, blank=True)
	graduate_country = models.CharField(max_length=100, null=True, blank=True)
	graduate_degree_obtained = models.CharField(max_length=1000, null=True, blank=True)
	graduate_major_subject = models.CharField(max_length=100, null=True, blank=False)
	graduate_marks_obtained = models.CharField(max_length=100, null=True, blank=True)
	graduate_date_of_completion = models.CharField(max_length=100, null=True, blank=True)

	ielts = models.CharField(max_length=100, blank=True, null=True)
	toefl = models.CharField(max_length=100, blank=True, null=True)
	sat = models.CharField(max_length=100, blank=True, null=True)
	gre = models.CharField(max_length=100, blank=True, null=True)
	gmat = models.CharField(max_length=100, blank=True, null=True)
	pte = models.CharField(max_length=100, blank=True, null=True)

	employment_current_employer = models.CharField(max_length=1000, blank=True, null=True)
	field_of_activity = models.CharField(max_length=1000,blank=True, null=True)
	position = models.CharField(max_length=100,blank=True, null=True)
	start_date = models.CharField(max_length=100,blank=True, null=True)
	department = models.CharField(max_length=100,blank=True, null=True)
	employment_type = models.CharField(max_length=100,blank=True, null=True)
	responsibilites = models.TextField(blank=True, null=True)

	previous_employer = models.CharField(max_length=1000,blank=True, null=True )	
	previous_location = models.CharField(max_length=1000, blank=True, null=True)
	previous_job_title = models.CharField(max_length=1000, blank=True, null=True)
	previous_start_date = models.CharField(max_length=1000, blank=True, null=True)
	previous_end_date = models.CharField(max_length=1000, blank=True, null=True)
	previous_employment_type = models.CharField(max_length=100, blank=True, null=True)

	question1 = models.CharField(max_length=1000, blank=True, null=True)
	question2 = models.CharField(max_length=1000, blank=True, null=True)
	question3 = models.CharField(max_length=1000, blank=True, null=True)
	question4 = models.CharField(max_length=1000, blank=True, null=True)
	question5 = models.CharField(max_length=1000, blank=True, null=True)
	question6 = models.CharField(max_length=1000, blank=True, null=True)
	question7 = models.CharField(max_length=1000, blank=True, null=True)
	question8 = models.CharField(max_length=1000, blank=True, null=True)

	statement_of_purpose = models.TextField(blank=True, null=True)

	photograph = models.ImageField(blank=True, null=True)
	resume = models.FileField(blank=True, null=True)
	passport_copy = models.FileField(blank=True, null=True)
	citizenship_copy = models.FileField(blank=True, null=True)
	school_education_certificate = models.FileField(blank=True, null=True)
	high_school_certificate = models.FileField(blank=True, null=True)
	undergrad_certificate = models.FileField(blank=True, null=True)
	graduate_certificate = models.FileField(blank=True, null=True)
	test = models.FileField(blank=True, null=True)

	certification = models.BooleanField()

	signature_name = models.CharField(max_length=100)
	date_of_signature = models.CharField(max_length=100)

	def __str__(self):
		name = self.first_name + " " + self.middle_name + " " + self.last_name
		return name