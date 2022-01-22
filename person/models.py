from email.policy import default
from pyexpat import model
from socket import NI_NOFQDN
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Person(models.Model):
    name = models.CharField (max_length=128)
    surname = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, blank = True, null= True)
    date_of_birth = models.DateField(default=None, blank= True, null=True)
    nif = models.IntegerField(blank=True, null=True)
    preferred_barber = models.ForeignKey('barber.barber', null=True, on_delete = models.SET_NULL )
    preferred_store = models.ForeignKey('store.store', null=True, on_delete = models.SET_NULL )

    class Meta:
        db_table = 'person'

    def get_absolute_url(self):
        return reverse('person:person-detail', kwargs={'id': self.id}) 
    