from django.db import models
from django.urls import reverse


class Barber(models.Model):
    name = models.CharField (max_length=128)
    surname = models.CharField(max_length=128)

    class Meta:
        db_table = 'barber'

    def get_absolute_url(self):
        return reverse('barber:barber-detail', kwargs={'id': self.id}) 
    