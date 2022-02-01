from email.policy import default
from pyexpat import model
from socket import NI_NOFQDN
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import IntegerField
from django.urls import reverse
#from phonenumber_field.modelfields import PhoneNumberField

class PersonManager(models.Manager):
    def create_person(self, name, surname, email, phone, date_of_birth, 
    nif, preferred_barber, preferred_store, is_active):

        person = self.create(name=name, surname=surname, email=email, phone=phone, date_of_birth=date_of_birth, 
                            nif=nif, preferred_barber=preferred_barber, preferred_store=preferred_store,
                             is_active=is_active)
        print('entrou')

        return person


class Person(models.Model):
    name = models.CharField (max_length=128)
    surname = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, blank = True, null= True)
    date_of_birth = models.DateField(default=None, blank= True, null=True)
    nif = models.IntegerField(blank=True, null=True)
    preferred_barber = models.ForeignKey('barber.barber', null=True, blank=True, on_delete = models.SET_NULL )
    preferred_store = models.ForeignKey('store.store', null=True, blank=True, on_delete = models.SET_NULL )
    is_active = models.BooleanField(default=True)

    objects = PersonManager()

    class Meta:
        db_table = 'person'

    def get_absolute_url(self):
        return reverse('person:person-detail', kwargs={'id': self.id}) 

