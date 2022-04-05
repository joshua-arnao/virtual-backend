from cgitb import html
from flask_restful import Resource, request
from dtos.registro_dto import ( RegistroDTO, 
                                UsuarioResponseDTO, 
                                LoginDTO)
from dtos.usuario_dto import ResetPasswordRequestDTO
from models.usuarios import Usuario
from config import conexion, sendgrid
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import environ
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import json
#from sendgrid.helpers.mail import Email, To, Content, Mail

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

class ResetPasswordController(Resource):
    def post(self):
        body = request.get_json()
        # ------------------------- UTILIZANDO LA LIBRERIA DE MENSAJERIA DE PYTHON -------------------------
        mensaje = MIMEMultipart()
        email_emisor = environ.get('EMAIL_EMISOR')
        print(email_emisor)
        email_password = environ.get('EMAIL_PASSWORD')
        try:
            data = ResetPasswordRequestDTO().load(body)
            # validar si existe ese usuario en mi bd
            usuarioEncontrado = conexion.session.query(
                Usuario).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is not None:
                # texto =  'Hola, este es un mensaje de prueba'
                mensaje['Subject'] = 'Reinciar contraseña Monedero APP'
                # Si quieres un generadpr de correos con diseño : https://beefree.io/
                # html='''<h2>Hola {} has solicitado el reinicio de tu contraseña de cuenta {}?</h2>
                #         <p>
                #         Si no has sido tu,entoces dale click al siguiente enlace: 
                #         <b><a>"{}/reset-password</a></b>
                #         </p>
                #         <p>Si no has sido tu entonces has caso omiso a este mensaje.</p>
                #         <br>
                #         <h3>Por favor no responder a este mensaje ya que es automatico.</h3>'''.format(usuarioEncontrado.nombre, usuarioEncontrado.correo, environ.get('URL_FRONT'))

                #Siempre que queremos agregar un HTML como textp del mensaje tiene que ir despues del texto ya que primero tratará de envriar el último y si no enviará en anteriors
                
                # ----------- ENCRIPTACIÓN DE INFORMACIÓN -----------
                # Fernet.generate_key() => para generar la llaveve que se guardara en el env
                fernet = Fernet(environ.get('FERNET_SECRET_KEY'))

                mensaje_secreto = {
                    'fecha_caducidad': str(datetime.now()+timedelta(hours=1)),
                    'id_usuario': usuarioEncontrado.id
                }

                mensaje_secreto_str = json.dumps(mensaje_secreto)
                mensaje_encriptado = fernet.encrypt(
                    bytes(mensaje_secreto_str,'utf-8'))

                # ----------- FIN DE ENCRIPTACION -----------

                # si queremos un generador de correos con diseño : https://beefree.io/
                html = open('./email_templates/prueba.html').read().format(
                    usuarioEncontrado.nombre, environ.get('URL_FRONT')+'/reset-password?token='+mensaje_encriptado.decode('utf-8'))

                # siempre que queremos agregar un HTML como texto del mensaje tiene que ir despues del texto ya que primero tratara de enviar el ultimo y si no puede enviara el anterior
                #mensaje.attach(MIMEText(texto, 'plain'))
                mensaje.attach(MIMEText(html, 'html'))

                # incio del envio del correo 
                #                       ||SERVIDOR | PUERTO
                # outlook => outlook.office365.com | 587
                # gmail => smtp.gmail.com          | 587
                # icloud => smtp.mail.me.com       | 587
                # yahoo => smtp.mail.yahoo.com     | 587
                # hotmail => smtp.live.com         | 587
                emisorSMTP = SMTP('smtp.gmail.com', 587)
                emisorSMTP.starttls()
                # Se hace el login de mi servidor de correo
                emisorSMTP.login(email_emisor, email_password)
                # envio de correo
                emisorSMTP.sendmail(
                    from_addr = email_emisor,
                    to_addrs = usuarioEncontrado.correo,
                    msg = mensaje.as_string()
                )
                # finalizo la sessión de mi correo
                emisorSMTP.quit()

                print('Correo enviado exitosamente')

            return {
                'message': 'Correo enviado exitosamente'
            }
        except Exception as e:
            print(e.args)
            return {
                'message': 'Error al enviar correo',
                'content': e.args
            }

        # ------------------------- UTILIZANDO SENDGRID -------------------------
        # try:
        #     data = ResetPasswordRequestDTO().load(body)
        #     # validar si existe ese usuario en mi bd
        #     usuarioEncontrado = conexion.session.query(
        #         Usuario).filter_by(correo=data.get('correo')).first()
        #     if usuarioEncontrado is not None:
        #         # tengo que utilizar los correos verificados en sendgrid ya que si uso uno que no esta verificado entonces el correo nunca llegara
        #         from_email = Email('joshua.arnao@icloud.com')
        #         to_email = To(usuarioEncontrado.correo)
        #         subject = 'Reinicia tu contraseña del Monedero App'
        #         content = Content(
        #             'text/plain', 'Hola, has solicitado el reinicio de tu contraseña, haz click en el siguiente link para cambiar, sino has sido tu ignora este mensaje: ....')
        #         mail = Mail(from_email, to_email, subject, content)
        #         envia_correo = sendgrid.client.mail.send.post(
        #             request_body=mail.get())
        #         # el estado de la respuesta de sendgrid
        #         print(envia_correo.status_code)
        #         # el cuerpo de la respuesta de sendgrid
        #         print(envia_correo.body)
        #         # las cabeceras de la respuesta de sendgrid
        #         print(envia_correo.headers)

        #     return {
        #         'message': 'Correo enviado exitosamente'
        #     }
        # except Exception as e:
        #     return {
        #         'message': 'Error al resetear la password',
        #         'content': e.args
        #     }