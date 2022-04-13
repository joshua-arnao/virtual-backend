from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    #? Clase que sirve para manejar el comportamiento del auth_user
    def create_user(self, correo, nombre, rol, password):
        #? Creación de un usuario sin el comando createsuperuser
        if not correo:
            raise ValueError('El usaurio debe tener obligatoriamente un correo')
        # normalize el correo => Aparte de validar que sea un correo valido removera los espacios inneesarios
        self.normalize_email(correo)
        # Manda a llamar el modelo Usuario e iniciara su construcción
        nuevoUsuario = self.model(correo = correo, nombre = nombre, rol = rol)
        # set_password => genera un hash de la contraseña usando bcrypt y el algoritmo SHA256
        nuevoUsuario.set_password(password)

        nuevoUsuario.save(using=self._db)
        return nuevoUsuario

    def create_superuser(self, correo, nombre, rol, password):
        usuario = self.create_user(correo, nombre, rol, password)

        usuario.is_superuser = True
        usuario.is_staff = True

        usuario.save(using=self._db)