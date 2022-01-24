
import pathlib
from django.urls import path

from store.views import StoreList, StoreDetail, StoreCreate, StoreUpdate, StoreDelete


#URLconf
app_name = 'store'
urlpatterns = [
    path('', StoreList.as_view(), name = 'store'),
    path('<int:pk>/', StoreUpdate.as_view(), name = 'store-detail'),
    path('create/', StoreCreate.as_view(), name = 'store-create'),
    path('<int:pk>/update', StoreUpdate.as_view(), name = 'store-uptdate'),
    path('<int:pk>/delete', StoreDelete.as_view(), name = 'store-delete'),
]
