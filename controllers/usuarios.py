from flask_restful import Resource, request
from dtos.registro_dto import ( RegistroDTO, 
                                UsuarioResponseDTO, 
                                LoginDTO)
from models.usuarios import Usuario
from config import conexion

class RegistroController(Resource):
    # Crear usuario
    def post(self):
        # get_jason => me da todo el body convertido en un diccionario
        body = request.get_json()
        try:
            data = RegistroDTO().load(body)
            nuevoUsuario = Usuario(**data)
            # Generar un hash de la contraseña
            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevoUsuario)
            return {
                'message': 'Usuario registrado exitosamente',
                'content': respuesta
            }, 201 # 201 => Usuario Creado
        except Exception as e:
            conexion.session.rollback() #Por si hubiera algún error
            return {
                'message': 'Error al registrar al usuario',
                'content': e.args
            }, 400 # 400 => Bad Request
        
class LoginController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = LoginDTO().load(body)
            return{
                'message': 'Bienvenido'
            }
        except Exception as e:
            return {
                'message': 'Credenciales incorrectas',
                'content': e.args
            }
