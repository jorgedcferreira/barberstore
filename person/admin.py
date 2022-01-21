from django.contrib import admin

#to be able to see the models in admin.py
from .models import Person

admin.site.register(Person)