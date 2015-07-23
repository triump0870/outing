from django import forms
from .models import User, PlaceChoice

# From class for the User 
class UserForm(forms.ModelForm):
	pickUpPlace = forms.ModelChoiceField(queryset=PlaceChoice.objects.all())
	class Meta:
		model = User
		exclude = ('phone_regex',)

	
