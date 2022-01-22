from dataclasses import field
from inspect import ClassFoundException
from sre_constants import SUCCESS
from django.shortcuts import render
from .forms import StoreForm
from .models import Store

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class StoreList(ListView):
    model = Store
    #template_name = 'store/store_list.html' <- default template name for List view
    #context_object_name = 'object_list' <- default name for List view


class StoreDetail(DetailView):
    model = Store

class StoreCreate(CreateView):
    model = Store
    fields = ['name', 'address', 'zip_code']
    success_url = reverse_lazy('store:store') #??

class StoreUpdate(UpdateView):
    model = Store
    fields = ['name', 'address', 'zip_code']
    success_url = reverse_lazy('store:store') #??

class StoreDelete(DeleteView):
    model = Store
    contex_object_name = 'store'
    success_url = reverse_lazy('store:store') #??


# def store_create_view(request):
#     form = StoreForm(request.POST or None)

#     if form.is_valid():
#         print(form.cleaned_data)
#         form.save()
#         form = StoreForm()
    
#     context = {
#         'form': form
#     }

#     return render(request, 'store/store_create.html', context)
