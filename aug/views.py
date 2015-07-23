from django.shortcuts import render
from django import forms
from .forms import UserForm
from .models import User
from django.views.generic.edit import FormView, UpdateView

# Create your views here.

# class UserView(UpdateView):
# 	template_name = 'registration.html'
# 	model = User
# 	form_class = UserForm
# 	success_url = '/thanks'

# 	def form_valid(self, form):
# 		self.object = form.save(commit=False)
# 		self.object.save()
# 		return render(self.template_name,self.get_context_data())

class UserView(FormView):
	template_name = 'new.html'
	model = User
	form_class = UserForm
	success_url = '/thanks'

	def form_valid(self, form):
		form.save(commit=True)
		return super(UserView, self).form_valid(form)