from email import contentmanager
from multiprocessing import context
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Person
from .forms import PersonForm
#from pubsub2 import observer
from pubsub import person_publisher
from django.http import JsonResponse
#from django_remot   e_forms.forms import RemoteForm



def person_detail_view(request, id):
    context = {
        'object' : Person.objects.get(id=id)
    }

    return render(request, 'person/person_detail.html', context = context)


def person_create_view(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
        obj = form.save()
        #observer.dispatch('PersonCreatedEvent', form.cleaned_data)
        person_publisher.dispatch('PersonCreatedEvent', form.cleaned_data)
        return redirect('../..{}'.format(obj.get_absolute_url()))
        
    
    context = {
        'form': form
    }
   
    return render(request, 'person/person_form.html', context)


def person_update_view(request, id):
    obj = get_object_or_404(Person, id=id)
    form = PersonForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('./') 
    
    context = {
        'form': form,
        'object': obj
        
    }



    return render(request, 'person/person_form.html', context)


def person_delete_view(request, id):
    obj = get_object_or_404(Person, id=id)
    
    if request.method == 'POST':
        obj.delete()
        print(reverse_lazy('person:person-list'))
        return redirect(reverse_lazy('person:person-list'))

    context = {
        'object': obj
    }

    return render(request, 'person/person_delete.html', context)


def person_list_view(request):
    queryset = Person.objects.all()

    context = {
        'object_list': queryset
    }

    return render(request, 'person/person_list.html', context = context)