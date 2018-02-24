from django.http import HttpResponse
import json


def MasterException(e):
	return HttpResponse(json.dumps({'error': "exception occurred"}))