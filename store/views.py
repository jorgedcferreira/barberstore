from dataclasses import field
from inspect import ClassFoundException
from sre_constants import SUCCESS
from django.shortcuts import render
from .models import Store
from .forms import StoreForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class StoreList(ListView):
    model = Store

class StoreDetail(DetailView):
    model = Store

class StoreCreate(CreateView):
    model = Store
    #fields = ['name', 'address', 'zip_code']
    form_class = StoreForm
    success_url = reverse_lazy('store:store') 

class StoreUpdate(UpdateView):
    model = Store
    #fields = ['name', 'address', 'zip_code']
    form_class = StoreForm
    #success_url = reverse_lazy('store:store') 

class StoreDelete(DeleteView):
    model = Store
    contex_object_name = 'store'
    success_url = reverse_lazy('store:store') 


