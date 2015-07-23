from .views import UserView
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$',UserView.as_view(), name='home'),
	url(r'^thanks/',TemplateView.as_view(template_name='success.html')),
	
	)

