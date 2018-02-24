from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=1000)
	unique_code = models.IntegerField(blank=True, null=True)
	barcode = models.ImageField(blank=True, null=True)
	description = models.TextField()
	price = models.IntegerField()
	organized_by = models.CharField(max_length=1000)
	date = models.CharField(max_length=10)
	time = models.CharField(max_length=10)
	picture = models.ImageField(blank=True, null=True)
	location = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=1000)
	email = models.EmailField()
	phone = models.CharField(max_length=100, null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name