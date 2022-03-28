# Tabla Foranea => La tabla no depende de otra tabla
from config import conexion
from sqlalchemy import Column, types
from bcrypt import hashpw, gensalt


class Usuario(conexion.Model):
    __tablename__ = 'usuarios'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(length=45))
    apellido = Column(type_=types.String(length=45))
    correo = Column(type_=types.String(length=45), nullable=False, unique=True)
    password = Column(type_=types.Text(), nullable=False)
    
    #Para usar el Hashing de la contraseña
    #https://pypi.org/project/bcrypt/
    def encriptar_pwd(self):
        #primero el password lo convierte a bytes
        password_bytes = bytes(self.password, 'utf-8')
        #usamos el metodo gensalt para genera un hash aleatorio y este se convinara con mi contraseña para generar un nuevo hach que ese será el que guardaremos en la  base de datos
        salt = gensalt(rounds=12) #predeterminado son 12 vueltas
        hash_password = hashpw(password_bytes, salt)
        #ahora lo convierno en string para guardarlo en la base de datos
        hash_pwd_string = hash_password.decode('utf-8')
        #sobre escribo el valor del password en la instacia por el generado
        self.password = hash_pwd_string