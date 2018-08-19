from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from main.models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.

def main(request):
    return render(request, 'main/main.html', {})

def newServi(request):
	if request.method == "POST":
		form = servicesForm(request.POST)
		if form.is_valid():
			servi = form.save(commit=False)
			servi.save()
			messages.success(request,'Servicio almacenado')
			return render(request, 'main/main.html')
	else:
		form = servicesForm()
	return render(request, 'main/newServi.html', {'form': form})

def newService(request):
	if request.method == "POST":
		form = newServiceForm(request.POST)
		if form.is_valid():
			customer = form.save()
			customer.save()
			messages.success(request,'Servicio almacenado')
			return render(request, 'main/main.html')
	else:
		form = newServiceForm()
		services = Services.objects.all()
	return render(request, 'main/newService.html', {'form': form})

def newCustomer(request):
	if request.method == "POST":
		form = customersForm(request.POST)
		if form.is_valid():
			customer = form.save(commit=False)
			customer.save()
			messages.success(request,'Cliente almacenado')
			return render(request, 'main/main.html')
	else:
		form = customersForm()
	return render(request, 'main/newCustomer.html', {'form': form})


def newTechnician(request):
	if request.method == "POST":
		form = techniciansForm(request.POST)
		if form.is_valid():
			customer = form.save(commit=False)
			customer.save()
			messages.success(request,'Técnico almacenado')
			return render(request, 'main/main.html')
	else:
		form = techniciansForm()
	return render(request, 'main/newTechnician.html', {'form': form})


def remissionHistory(request):
	query = request.GET.get('q')
	
	if query:
		remision = registeredServices.objects.filter(remission__icontains=query).order_by('date')
		return render(request, 'main/remissionHistory.html', {'info':remision})
	remision = registeredServices.objects.all().order_by('date')
	return render(request, 'main/remissionHistory.html', {'info':remision})

def customerHistory(request):
	return render(request, 'main/customerHistory.html')

def techniciansHistory(request):
	return render(request, 'main/techniciansHistory.html')

def configuration(request):
	return render(request, 'main/configuration.html')

def customer_detail(request,pk):
    customer = get_object_or_404(customers, CCNIT=pk)
    return render(request, 'main/customer_detail.html', {'customer': customer})

def technician_detail(request,pk):
    technician = get_object_or_404(Technicians, id_person=pk)
    return render(request, 'main/technician_detail.html', {'technician': technician})

def remission_detail(request,pk):
    remission = get_object_or_404(registeredServices, remission=pk)
    services = remission.service.all()
    return render(request, 'main/remission_detail.html', {'remission' : remission , 'services' : services})

