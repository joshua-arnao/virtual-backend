from django.db import models
# AbstractBaseUser => modifica todo el modelo auth_user desde cero
# AbstractUser => Permite agregar nuevas columnas de las que ya estaban creadas incialmente
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from autorizacion.authManager import UserManager

# Create your models here.


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=45, null=False)
    rol = models.CharField(choices=(
        # con la cual se usara en la bd y se mostrara | la que se usara para los formularios
        ['ADMINISTRADOR', 'ADMINISTRADOR'],
        ['MOZO', 'MOZO']), max_length=40)

    # si queremos seguir utilizando el panel administrativo entonces deberemos declarar las siguientes columnas
    # is_staff > indicara si el usuario creado puede acceder o no al panel administrativo (es parte del equipo)
    is_staff = models.BooleanField(default=False)
    # is_active > puede realizar operaciones dentro del panel administrativo, si el usuario no esta activo podra logearse pero no podra realizar ninguna acci
    is_actived = models.BooleanField(default=True)

    createAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    # comportamiento que tendra el modelo cuando se realice el comando createsuperuser
    objects = UserManager()

    USERNAME_FIELD = 'correo'
    # comentario prueba
    REQUIRED_FIELDS = ['nombre', 'rol']

    class Meta:
        db_table = 'usuarios'
