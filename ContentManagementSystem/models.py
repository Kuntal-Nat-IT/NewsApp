from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.

class Faq(models.Model):
	question 	= 	models.CharField(max_length=300, null=True)
	answer   	= 	models.TextField(null=True)
	createdOn	= 	models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural='Frequently Asked Questions (FAQs)'

	def __str__(self):
		return self.question


