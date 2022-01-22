from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Appointment

class AppointmentList(ListView):
    model = Appointment

class AppointmentDetail(DetailView):
    model = Appointment

class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['person', 'store', 'barber', 'date', 'time']
    success_url = reverse_lazy('schedulle:appointment-detail')

class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = ['person', 'store', 'barber', 'date', 'time']
    success_url = reverse_lazy('schedulle:appointment-detail')

class AppointmentDelete(DeleteView):
    model = Appointment
    contex_object_name = 'store'
    success_url = reverse_lazy('schedulle:appointment-list') 

