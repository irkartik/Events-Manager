from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Branch(models.Model):
	name = models.CharField(max_length=100)
	address = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Branch'
		verbose_name_plural = 'Branches'

class AuthUser(AbstractUser):
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "Staff User"
		verbose_name_plural = "Staff Users"

class Event(models.Model):
	name = models.CharField(max_length=1000)
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	unique_code = models.IntegerField(blank=True, null=True)
	barcode = models.ImageField(blank=True, null=True)
	description = models.TextField()
	price = models.IntegerField()
	organized_by = models.CharField(max_length=1000)
	date = models.CharField(max_length=10)
	time = models.CharField(max_length=10)
	picture = models.ImageField()
	location = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=1000)
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	email = models.EmailField()
	phone = models.CharField(max_length=100, null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name