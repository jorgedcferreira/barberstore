import pathlib
from django.urls import path

from person.views import ( 
    person_update_view,
    person_delete_view,
    person_list_view,
    person_create_view
)


#URLconf
app_name = 'person'
urlpatterns = [
    path('create/', person_create_view, name='person-create'),
    path('<int:id>/', person_update_view, name = 'person-detail'),
    path('<int:id>/delete/', person_delete_view, name='person-delete'),
    path('', person_list_view, name='person-list')
]
