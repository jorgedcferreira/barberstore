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
    height = models.DecimalField(max_digits=3, decimal_places=2)
    date_of_birth = models.DateField(default=None)
    id_number = models.IntegerField(
        validators=[
            MaxValueValidator(99999999), 
            MinValueValidator(0)
            ]   
        )
    is_alive = models.BooleanField(default=True)
    nif = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'person'

    def get_absolute_url(self):
        return reverse('person:person-detail', kwargs={'id': self.id}) 
    