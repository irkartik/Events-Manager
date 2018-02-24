from django.http import HttpRequest
import json

def MasterException(e):
	return HttpRequest(json.dumps('error': "chutiya katgaya"))