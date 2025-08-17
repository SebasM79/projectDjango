
from django.urls import path
from . import views

urlpatterns = [
    path('crear_editorial/', views.crear_editorial, name='crear_editorial'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    
]
