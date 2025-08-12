
from django.urls import path
from . import views

urlpatterns = [
      path('', views.hello),
    path('seba/', views.seba),
    path('home/', views.home),
    path('about/', views.about),  # Nueva ruta para la vista 'about'
]