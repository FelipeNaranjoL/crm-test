from django.contrib.auth.models import User
from django.db import models

# modelo para usuario

class Usuarios(models.Model):
    user = models.OneToOneField(User, related_name = 'usuario', on_delete=models.CASCADE)