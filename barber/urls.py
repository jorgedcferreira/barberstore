import pathlib
from django.urls import path

from barber.views import ( 
    barber_update_view,
    barber_delete_view,
    barber_list_view,
    barber_create_view,
    barber_detail_view
    
)


#URLconf
app_name = 'barber'
urlpatterns = [
    path('create/', barber_create_view, name='barber-create'),
    path('<int:id>/update', barber_update_view, name = 'barber-update'),
    path('<int:id>/', barber_detail_view, name = 'barber-detail'),
    path('<int:id>/delete/', barber_delete_view, name='barber-delete'),
    path('<int:id>/', barber_delete_view, name='barber-delete'),
    path('', barber_list_view, name='barber-list')
]
