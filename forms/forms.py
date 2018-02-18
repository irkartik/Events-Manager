from django.forms import ModelForm
from .models import *

class CheckYourEligibilityForm(ModelForm):
	class Meta:
		model = CheckYourEligibility