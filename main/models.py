from django.db import models
from django.utils import timezone
# Create your models here.

class Technicians(models.Model):
    IDD = models.AutoField(primary_key=True)
    id_person = models.CharField(max_length=200,unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address =  models.CharField(max_length=200,default=' ')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class customers(models.Model):
    IDD = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    CCNIT = models.CharField(max_length=200,unique=True)
    Department = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    ext = models.CharField(max_length=200,blank=True,default='0')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Services(models.Model):
    IDD = models.AutoField(primary_key=True)
    ID_service = models.CharField(max_length=200,unique=True)
    service = models.CharField(max_length=200)
    value = models.FloatField()

    def __str__(self):
        strr = self.ID_service+' '+self.service+' '+str(self.value)
        return strr

    class Meta:
        ordering = ('service',)    

class registeredServices(models.Model):
    IDD = models.AutoField(primary_key=True)
    remission = models.CharField(max_length=200,unique=True)
    billNum = models.CharField(max_length=200,blank=True,default=' ')
    dateBill = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)
    dateService = models.DateTimeField(default=timezone.now)
    technician = models.ForeignKey(Technicians, on_delete=models.CASCADE)
    service  = models.ManyToManyField(Services)
    Observation = models.CharField(max_length=200,default='Ninguna')
    stateRemission = models.IntegerField(blank=True,default=0)
    paidOut = models.FloatField(blank=True,default=0.0)
    residue = models.FloatField(blank=True,default=0.0)
    estateBill = models.IntegerField(blank=True,default=0)

    class Meta:
        ordering = ('remission',)


class SpecificServices(models.Model):
    IDD = models.AutoField(primary_key=True)
    remission = models.ForeignKey(registeredServices, on_delete=models.CASCADE)
    amount = models.IntegerField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    value = models.FloatField()
    total =models.FloatField()
    generalTotal = models.FloatField()
    IVA = models.FloatField()
    RETEIVA = models.FloatField()
    RETEICA = models.FloatField()
    RETEFUENTE = models.FloatField()
    generalTotalWithTax = models.FloatField()

    class Meta:
        ordering = ('remission',)