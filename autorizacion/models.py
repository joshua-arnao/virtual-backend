from django.db import models
#AbstractBaseUser => modifica todo el modelo auth_user desde cero
#AbstractUser => Permite agregar nuevas columnas de las que ya estaban creadas incialmente
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=45, null=False)
    rol = models.CharField(choices=(
        ['ADMINISTRADOR', 'ADMINISTRADOR']
        ['MOZO', 'MOZO']
    ), max_length=40)


is_staff = models.BooleanField(default=False)
is_active = models.BooleanField(default=True)

createAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

objects = None
