"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from flora import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # ARTIST
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/create/', views.artist_create, name='artist_create'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('artists/<int:artist_id>/edit/', views.artist_edit, name='artist_edit'),
    path('artists/<int:artist_id>/delete/', views.artist_delete, name='artist_delete'),
    path('artists/country/<str:country>/', views.artist_list_by_country, name='artist_list_by_country'),

    # INSTALLATION
    path('installations/', views.installation_list, name='installation_list'),
    path('installations/create/', views.installation_create, name='installation_create'),
    path('installations/<int:installation_id>/', views.installation_detail, name='installation_detail'),
    path('installations/edition/<int:edition_id>/', views.installation_list_by_edition, name='installation_list_by_edition'),
    path('installations/order/<str:order>/', views.installation_list_by_opening_date, name='installation_list_by_opening_date'),

    # VENUE
    path('venues/', views.venue_list, name='venue_list'),
    path('venues/create/', views.venue_create, name='venue_create'),
    path('venues/<int:venue_id>/', views.venue_detail, name='venue_detail'),

    # EDITION
    path('editions/', views.edition_list, name='edition_list'),
    path('editions/create/', views.edition_create, name='edition_create'),
    path('editions/<int:edition_id>/', views.edition_detail, name='edition_detail'),
    
    #HOME
    path('', views.home, name='home'),
]
