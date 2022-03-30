from flask import Flask, render_template
from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import Api
from controllers.usuarios import (  LoginController, 
                                    RegistroController,
                                    ResetPasswordController)
from config import validador, conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from dtos.registro_dto import UsuarioResponseDTO
from seguridad import autenticador, identificador
from datetime import timedelta
from seed import categoriaSeed
from controllers.movimientos import MovimientoController

#cargar la libreria
load_dotenv()

app = Flask(__name__)
CORS(app = app)


app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
#para cambiar el endpoint de mi JWT
app.config['JWT_AUTH_URL_RULE'] = '/login-jwt'
# para cambiar la llave para solicitar el username
app.config['JWT_AUTH_USERNAME_KEY'] = 'correo'
# para cambiar la llave para solicitar la password
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pass'
# para cambiar el tiempo de expiracion de mi JWT
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1, minutes=5)
# Para indicar cual sera el prefijo de la token en los headers de authorization
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearear'
jsonwebtoken = JWT(app=app, authentication_handler=autenticador,
                    identity_handler=identificador)

api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)

#conexion.drop_all(app=app) # Eliminara todos los registros de una tabla
conexion.create_all(app=app)

#Ingresará antes de hacer el primer request a nuesntra función, tola la lógica que queremos que se haga antes de la primera
@app.before_first_request
def seed():
    'Ahora hacemos el seed de las tablas respectivas'
    categoriaSeed()

@app.route('/')
def inicio():
    # render_template > renderiza un archivo .html o .jinja para q flask lo pueda leer e interpretar al cliente
    return render_template('inicio.html', nombre='Eduardo', dia='Jueves', integrantes=[
        'Foca',
        'Lapagol',
        'Ruidiaz',
        'Paolin',
        'Rayo Advincula'
        ], usuario= {
            'nombre':'Juan',
            'direccion': 'Las piedritas 105',
            'edad': '40'
        }, selecciones = [{
            'nombre':'Bolivia',
            'clasificado': False
        },{
            'nombre': 'Brasil',
            'clasificado': True
        },{
            'nombre': 'Chile',
            'clasificado': False
        },{
            'nombre': 'Peru',
            'timado': True
        }])

# Al colocar jwt_required estamos indicando que para ese controlador se deberá proveer una JWT valida
@app.route('/yo')
@jwt_required()
def perfil_usuario():
    print(current_identity)
    usuario = UsuarioResponseDTO().dump(current_identity)
    return {
        'message': 'El usuario es',
        'content': usuario
    }
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(MovimientoController, '/movimiento', '/movimientos')
api.add_resource(ResetPasswordController, '/reset-password')

if(__name__ == '__main__'):
    app.run(debug=True)