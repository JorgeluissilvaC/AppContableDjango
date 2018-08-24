from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from main.models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.

def main(request):
    return render(request, 'main/main.html', {})
def delete(request):
	if request.method == "GET":
		IDD = request.GET.get('IDD')
		tipo = request.GET.get('tipo')
		if tipo=='1':
			custo = get_object_or_404(Services, IDD=IDD)
		if tipo=='2':
			custo = get_object_or_404(customers, IDD=IDD)
		if tipo=='3':
			custo = get_object_or_404(Technicians, IDD=IDD)

		custo.delete()
		messages.success(request,'Información borrada')

def SaveServi(request):
	if request.method == "GET":
		IDD = request.GET.get('IDD')
		custo = get_object_or_404(Services, IDD=IDD)
		custo.ID_service = request.GET.get('ID_service')
		custo.service = request.GET.get('service')
		custo.value = float(request.GET.get('value').replace(',','.'))
		custo.save()
		messages.success(request,'Técnico actualizado')

	return render(request, 'main/main.html', {})

def SaveTecnician(request):
	if request.method == "GET":
		IDD = request.GET.get('IDD')
		custo = get_object_or_404(Technicians, IDD=IDD)
		custo.id_person = request.GET.get('id_person')
		custo.name = request.GET.get('name')
		custo.phone = request.GET.get('phone')
		custo.save()
		messages.success(request,'Servicio actualizado')

	return render(request, 'main/main.html', {})

def SaveCustomer(request):
	if request.method == "GET":
		IDD = request.GET.get('IDD')
		custo = get_object_or_404(customers, IDD=IDD)
		print(custo.name)
		custo.name = request.GET.get('name')
		custo.CCNIT = request.GET.get('CCNIT')
		custo.Department = request.GET.get('Department')
		custo.city = request.GET.get('city')
		custo.cell = request.GET.get('cell')
		custo.address = request.GET.get('address')
		custo.phone = request.GET.get('phone')
		custo.ext = request.GET.get('ext')
		custo.save()
		messages.success(request,'Cliente actualizado')

	return render(request, 'main/main.html', {})

def customerList(request):
	query = request.GET.get('q')
	if query:
		info = customers.objects.filter(name__icontains=query)
		return render(request, 'main/customerList.html', {'info':info})

	info = customers.objects.all()
	return render(request, 'main/customerList.html',{'info':info})

def technicianList(request):
	query = request.GET.get('q')
	if query:
		info = Technicians.objects.filter(name__icontains=query)
		return render(request, 'main/technicianList.html', {'info':info})

	info = Technicians.objects.all()
	return render(request, 'main/technicianList.html',{'info':info})

def servicesList(request):
	query = request.GET.get('q')
	if query:
		info = Services.objects.filter(ID_service__icontains=query)
		return render(request, 'main/servicesList.html', {'info':info})

	info = Services.objects.all()
	return render(request, 'main/servicesList.html',{'info':info})
	
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

def servi_detail(request,pk):
    remission = get_object_or_404(Services, ID_service=pk)
    return render(request, 'main/servi_detail.html', {'remission' : remission})
