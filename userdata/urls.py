from django.urls import path
from . import views

urlpatterns = [
	path('make-an-appointment', views.create_appointment, name="make-an-appointment"),
	path('show_appointments', views.show_appointments, name="show_appointments"),

	path('check-eligibility', views.create_check_eligibility, name="check-eligibility"),
	path('show_eligibility', views.show_eligibility, name="show_eligibility"),

	path('apply-now', views.apply_now, name="apply_now"),
	path('show_applied_users', views.show_applied_users, name="show_applied_users"),
	path('<int:user_id>/full_profile', views.show_full_profile, name="show_full_profile")
]