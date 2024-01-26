from django.contrib import admin

from .models import SensorData,UserData

# # Register your models here.

admin.site.register(SensorData)
admin.site.register(UserData)