
import pathlib
from django.urls import path

from .views import AppointmentList, AppointmentDetail, AppointmentCreate, AppointmentUpdate, AppointmentDelete


#URLconf
app_name = 'schedule'
urlpatterns = [
    path('', AppointmentList.as_view(), name = 'appointment'),
    path('<int:pk>/', AppointmentDetail.as_view(), name = 'appointment-detail'),
    path('create/', AppointmentCreate.as_view(), name = 'appointment-create'),
    path('<int:pk>/update', AppointmentUpdate.as_view(), name = 'appointment-uptdate'),
    path('<int:pk>/delete', AppointmentDelete.as_view(), name = 'appointment-delete'),
]
