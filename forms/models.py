from django.db import models

# Create your models here.

class CheckYourEligibility(models.Model):
	name = models.CharField(max_length=1000)
	email = models.EmailField()
	address = models.TextField()
	phone = models.PositiveIntegerField()
	qualification = models.CharField(max_length=100)
	ielts = models.PositiveIntegerField()
	toefl = models.PositiveIntegerField()
	sat = models.PositiveIntegerField()
	gre = models.PositiveIntegerField()
	gmat = models.PositiveIntegerField()
	pte = models.PositiveIntegerField()
	priority_country = models.CharField()
	remarks = models.TextField()

	def __str__(self):
		return name.self