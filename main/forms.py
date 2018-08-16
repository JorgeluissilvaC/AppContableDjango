from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class customersForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ( 'CCNIT','name','Department','city','address','cell','phone','ext',)

class techniciansForm(forms.ModelForm):
    class Meta:
        model = Technicians
        fields = ( 'id_person','name','phone','address',)

class servicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ( 'ID_service','service','value',)

class newServiceForm(forms.ModelForm):
    class Meta:
        model = registeredServices
        fields = ( 'remission','date','customer','dateService','technician','service','Observation','stateRemission',)
        widgets = {
            'date': DateInput(),
            'dateService': DateInput(),
        }