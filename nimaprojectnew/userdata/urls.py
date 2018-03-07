from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^make-an-appointment$', views.create_appointment, name="make-an-appointment"),
	url(r'^appointments/show$', views.show_appointments, name="show_appointments"),
	url(r'^appointments/show/(?P<appointment_id>[0-9]+)', views.full_appointment, name="full_appointment"),

	url(r'^check-eligibility$', views.create_check_eligibility, name="check-eligibility"),
	url(r'^eligibility/show$', views.show_eligibility, name="show_eligibility"),
	url(r'^eligibility/show/(?P<eligibility_id>[0-9]+)$', views.full_eligibility, name="full_eligibility"),	

	url(r'^apply-now$', views.apply_now, name="apply_now"),
	url(r'^applied_users/show$', views.show_applied_users, name="show_applied_users"),
	url(r'^applied_users/show/(?P<user_id>[0-9]+)$', views.show_full_profile, name="show_full_profile")
]