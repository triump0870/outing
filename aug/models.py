from django.db import models
from django.core.validators import RegexValidator
from django.utils.functional import lazy

# Constants
REGION_CHOICE = (
	('South','South'),
	('North','North'),
)
class NorthPlaceChoice(models.Model):
	place = models.CharField(max_length=30)

	def __unicode__(self):
		return self.place

class SouthPlaceChoice(models.Model):
	place = models.CharField(max_length=30)

	def __unicode__(self):
		return self.place

class User(models.Model):
	"""
	User model for employees.
	"""

	name = models.CharField(verbose_name='Full Name',max_length=150,blank=False,null=False)
	signum = models.CharField(max_length=10, blank=False, null=False)
	email = models.EmailField(verbose_name='Email (Ericsson mail address)',max_length=150,blank=False,null=False, unique=True)
	phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '9012345678'. Up to 10 digits allowed.")
	phone_number = models.CharField(max_length=10, validators=[phone_regex], blank=False, null=False) # validators should be a list
	region = models.CharField(max_length=10,blank=False, null=False, choices=REGION_CHOICE)	
	northPickUpPlace = models.ForeignKey(NorthPlaceChoice,verbose_name='PickUpPlace',related_name='PickUpPlace')
	southPickUpPlace = models.ForeignKey(SouthPlaceChoice, verbose_name='PickUpPlace')
	comments = models.TextField(verbose_name='Comments (Optional)',blank=True, null=True)

	def __unicode__(self):
		return self.name