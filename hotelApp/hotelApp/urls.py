"""
URL configuration for hotelApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from hoteles import views
from clientApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listaHotel, name='listaHotel'),
    path('creaHotel', views.crearHotel, name='crearHotel'),
    path('editarHotel/<int:id>/', views.editarHotel, name='editarHotel'),
    path('eliminarHotel/<int:id>/', views.eliminarHotel, name='eliminarHotel'),
    path('listaClient', views.listaClient, name='listaClient'),
    path('crearClient', views.crearClient, name='crearClient'),
    path('editarClient/<int:id>/', views.editarClient, name='editarClient'),
    path('eliminarClient/<int:id>/',views.eliminarClient, name='eliminarClient'),
]