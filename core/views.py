from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Event

# Create your views here.

def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			return redirect('user_login')
	else:
		context = {}
		return render(request, 'core/login_form.html', context)	

@login_required(login_url='/login/')
def logout_user(request):
	logout(request)
	return redirect('login')

@login_required(login_url='/login/')
def dashboard(request):
	context = {
		'events' : Event.objects.all(),
	}
	return render(request, 'core/show_events.html', context)

@login_required(login_url="/login/")
def create(request):
	if request.method=="POST":
		name = request.POST.get("name")
		description = request.POST.get("description") 
		price = request.POST.get("price")
		organized_by = request.POST.get("organizer")
		date = request.POST.get("date")
		time = request.POST.get("time")
		image = request.FILES["image"]
		location = request.POST.get("location")

		temp = Event.objects.create(name=name, description=description, price=price, organized_by=organized_by, date=date, time=time, picture=image, location=location)

		return redirect('dashboard')
	else:
		context = {}
		return render(request, 'core/create_event.html', context)

@login_required(login_url="/login/")
def delete_event(request, event_id):
	temp = Event.objects.get(id=event_id)
	temp.delete()

	return redirect('dashboard')

@login_required(login_url="/login/")
def update_event(request, event_id):
	if request.method=="POST":
		name = request.POST.get("name")
		description = request.POST.get("description") 
		price = request.POST.get("price")
		organized_by = request.POST.get("organizer")
		date = request.POST.get("date")
		time = request.POST.get("time")
		image = request.FILES["image"]
		location = request.POST.get("location")
		print(request.FILES)
		temp = Event.objects.get(id=event_id)

		if image is not None:
			temp.picture = image
			
		temp.name = name 
		temp.description = description 
		temp.price = price 
		temp.organized_by = organized_by 
		temp.date = date 
		temp.time = time 
		temp.location = location 
		temp.save()

		return redirect('dashboard')
	else:
		context = {
			'event': Event.objects.get(id=event_id),
		}
		return render(request, 'core/event_update.html', context)