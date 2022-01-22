from django.db import models
from django.urls import reverse

class Appointment(models.Model):
    person = models.ForeignKey('person.person', null=True, on_delete = models.SET_NULL )
    store = models.ForeignKey('store.store', null=True, on_delete = models.SET_NULL )
    barber = models.ForeignKey('barber.barber', null=True, on_delete = models.SET_NULL )
    date = models.DateField ()
    time = models.TimeField()


    class Meta:
        db_table = 'Appoitment'

    def get_absolute_url(self):
         return reverse('schedule:appointment-detail', kwargs={'pk': self.id}) 