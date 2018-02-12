from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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

def logout_user(request):
	logout(request)
	return redirect('login')

def dashboard(request):
	return HttpResponse('Dashboard')