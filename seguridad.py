from config import conexion
from models.usuarios import Usuario
from bcrypt import checkpw

def autenticador(username, password):
    """Función emcargada de validar sin las credenciales son correctas o no, si no son no pasara pero si si lo son retornara JWT"""
    #Primero validamos que los parametros sean correctos
    if username and password:
        #Buscare el usuario en la base de ddatos
        usuarioEncontrado = conexion.session.query(
            Usuario).filter_by(correo=username).first()
        if usuarioEncontrado:
            #ahora valiso si la password es la correcta
            validacion = checkpw(   bytes(password, 'utf8'),
                                    bytes(usuarioEncontrado.password, 'utf8'))
            if validacion is True:
                print('si es la contraseña')
                # si todas las validaciones son correctas entonces deberemos de retornar una instancia con un atributo id
                return usuarioEncontrado
            else:
                return None
        else:
            return None
    else:
        return None


def identificador(payload):
    #Sirve para validar el usuario previamente autenticado
    #En el payload tendremos la parte intermedia del JET que es la inforamción que se puede visualizar sin la necesidad de saber la contraseña de la token
    #identity => la identificación del usuario (por lo general viene a ser el ID o UUID del mismo)
    #SELECT * form WHERE
    print(payload)
    usuarioEncontrado: Usuario | None = conexion.session.query(
        Usuario).filter_by(id = payload['identity']).first()
    if usuarioEncontrado:
        # esta informacion me servira para cuando quiera acceder al usuario actual de la peticion
        return usuarioEncontrado
    else:
        return None