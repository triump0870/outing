from django import forms
from django.views.generic.edit import FormView

from .forms import UserForm
from .models import User
# Create your views here.

class UserView(FormView):
	template_name = 'new.html'
	model = User
	form_class = UserForm
	success_url = '/thanks'

	def form_valid(self, form):
		form.save(commit=True)
		return super(UserView, self).form_valid(form)
