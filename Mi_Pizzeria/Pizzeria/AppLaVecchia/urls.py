"""
URL configuration for Pizzeria project.

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
from django.urls import path
from AppLaVecchia import views
from AppLaVecchia import class_views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('menu/', views.menu,name="Menu"),
    path('reservas/', views.reservas,name="Reservas"),
    path('contacto/', views.contacto,name="Contacto"),
      
   
]

urlpatterns += [
    path('class-list/', class_views.CursoListView.as_view(), name="List"),
    path('class-detail/<pk>/', class_views.CursoDetailView.as_view(), name="Detail"),
    path('class-create/', class_views.CursoCreateView.as_view(), name="Create"),
    path('class-update/<pk>/', class_views.CursoUpdateView.as_view(), name="Update"),
    path('class-delete/<pk>/', class_views.CursoDeleteView.as_view(), name="Delete"),
]

