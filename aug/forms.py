from django import forms
from .models import User, NorthPlaceChoice

# From class for the User 
class UserForm(forms.ModelForm):
	pickUpPlace = forms.ModelChoiceField(queryset=NorthPlaceChoice.objects.all())
	class Meta:
		model = User
		exclude = ('phone_regex',)

	
