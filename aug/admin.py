from django.contrib import admin
from .models import User, NorthPlaceChoice, SouthPlaceChoice
# Register your models here.

admin.site.register(User)
admin.site.register(NorthPlaceChoice)
admin.site.register(SouthPlaceChoice)