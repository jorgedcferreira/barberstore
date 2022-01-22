from django.db import models
from django.urls import reverse

class Store(models.Model):
    name = models.CharField (max_length=128)
    address = models.CharField (max_length=128)
    zip_code = models.CharField (max_length=16)


    class Meta:
        db_table = 'store'

    def get_absolute_url(self):
         return reverse('store:store-detail', kwargs={'pk': self.id}) 
    