from django.urls import path
from .views import inicio

# Serán todas las rutas de esta aplicación las tendremos que registrar aquí solamente se puede usar esta variables de
urlpatterns = [
    path('inicio', inicio)
]