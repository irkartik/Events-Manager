from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^make-an-appointment', views.create_appointment, name="make-an-appointment"),
	url(r'^show_appointments', views.show_appointments, name="show_appointments"),
	url(r'^(?P<appointment_id>[0-9])/full_appointment', views.full_appointment, name="full_appointment"),

	url(r'^check-eligibility', views.create_check_eligibility, name="check-eligibility"),
	url(r'^show_eligibility', views.show_eligibility, name="show_eligibility"),

	url(r'^apply-now', views.apply_now, name="apply_now"),
	url(r'^show_applied_users', views.show_applied_users, name="show_applied_users"),
	url(r'^(?P<user_id>[0-9])/full_profile', views.show_full_profile, name="show_full_profile")
]