"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import pathlib
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
import storefront.settings as settings


urlpatterns = [
    #path('', home_view, name='home'),
    #path('home/', home_view, name='home'),
    #path('contacts/', contact_view, name='contacts'),
    #path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
    path('person/', include('person.urls')),
    # path('persons/create/', person_create_view, name='create_person'),
    # path('persons/<int:id>/', person_update_view, name = 'person-detail'),
    # path('persons/<int:id>/delete/', person_delete_view, name='person-delete'),
    # path('persons/', person_list_view, name='person-list')
]

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [path(r'__debug__/', include(debug_toolbar.urls))]
    except ImportError:
        pass