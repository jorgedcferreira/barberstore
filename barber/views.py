from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Barber
from .forms import BarberForm


def barber_detail_view(request, id):
    context = {
        'object' : Barber.objects.get(id=id)
    }

    return render(request, 'barber/barber_detail.html', context = context)


def barber_create_view(request):
    form = BarberForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save()   
        return redirect('../..{}'.format(obj.get_absolute_url()))
    
    context = {
        'form': form
    }

    return render(request, 'barber/barber_form.html', context)


def barber_update_view(request, id):
    obj = get_object_or_404(Barber, id=id)
    form = BarberForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = BarberForm(request.POST or None, instance=obj)
    
    context = {
        'form': form,
        'object' : obj
    }

    return render(request, 'barber/barber_form.html', context)


def barber_delete_view(request, id):
    obj = get_object_or_404(Barber, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
        

    context = {
        'object': obj
    }

    return render(request, 'barber/barber_delete.html', context)


def barber_list_view(request):
    queryset = Barber.objects.all()

    context = {
        'object_list': queryset
    }

    return render(request, 'barber/barber_list.html', context)


