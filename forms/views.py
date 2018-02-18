from django.shortcuts import render
from .models import Eligibility, Appointment
# Create your views here.


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

		temp = Appointment.objects.create(name=name, description=description, price=price, organized_by=organized_by, date=date, time=time, picture=image, location=location)
		temp.save()

		return redirect('dashboard')
	else:
		context = {}
		return render(request, 'forms/create_appointment_form.html', context)



