"""
URL configuration for Act_Semanal_21_11 project.

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
from ventas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/crear/', views.crear_cliente_view),  # nombre correcto
    path('clientes/activos/', views.mostrar_clientes_activos),
    path('clientes/<int:id>/pedidos/', views.mostrar_clientes_con_pedidos),
    path('clientes/', views.mostrar_clientes),  # ojo: aquí también estaba mal escrito
    path('pedidos/estado/<str:estado>', views.mostrar_pedidos_por_estado),
    path('pedidos/cliente/<int:id>', views.mostrar_pedidos_cliente_concreto),
    path('clientes/totalpagado/', views.mostrar_total_pagado_por_cliente),
    path('pedidos/pagado/<str:codigo>', views.marcar_pedido_pagado),
    path('pedidos/crear/', views.crear_nuevo_pedido),
]