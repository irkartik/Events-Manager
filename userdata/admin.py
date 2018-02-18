from django.contrib import admin
from .models import Appointment, Eligibility, AppliedUser
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Eligibility)
admin.site.register(AppliedUser)