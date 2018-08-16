from django.contrib import admin
from .models import customers,Technicians,SpecificServices,registeredServices,Services

admin.site.register([customers,Technicians,SpecificServices,registeredServices,Services])