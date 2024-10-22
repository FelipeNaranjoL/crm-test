from django.contrib import admin

# declaramos el modelo Usuarios para visualizarlo en modo admin
from .models import Usuarios

admin.site.register(Usuarios)