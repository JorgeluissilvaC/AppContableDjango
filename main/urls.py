from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main,name='main'),
    url(r'^newService/$', views.newService),
    url(r'^newCustomer/$', views.newCustomer,name='newCustomer'),
    url(r'^newTechnician/$', views.newTechnician),
    url(r'^newServi/$', views.newServi),

    url(r'^remissionHistory/$', views.remissionHistory),
    url(r'^customerHistory/$', views.customerHistory),    
    url(r'^techniciansHistory/$', views.techniciansHistory), 
    url(r'^configuration/$', views.configuration), 
    url(r'^customer/(?P<pk>[0-9]+)/$', views.customer_detail, name='customer_detail'),
    url(r'^technician/(?P<pk>[0-9]+)/$', views.technician_detail, name='technician_detail'),
    url(r'^remission/(?P<pk>[0-9]+)/$', views.remission_detail, name='remission_detail'),
    
       
    ]