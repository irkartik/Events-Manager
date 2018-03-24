from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Branch(models.Model):
	name = models.CharField(max_length=100)
	address = models.TextField()

	def __str__(self):
		return self.name

class AuthUser(AbstractUser):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "AuthUser"

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