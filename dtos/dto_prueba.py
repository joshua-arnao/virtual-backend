from config import validador
from marshmallow import fields, validate

class ValidadorPrueba(validador.Schema):
    nombre = fields.Str(validate=validate.Length(max=10))
    apellido = fields.Str()
    edad = fields.Int()
    soltero = fields.Bool()

    #Es una clase que va a ser para poder pasar parametros a la metadata del padre (De la clase de la cual esamos heredando), deifinimoos atributos que van a ser la clase schema para poder hacer ña validación correcta
    # class Meta:
    #     #En el atributo fields iran lo que sería que valores necesitamos
    #     fields = ['nombre', 'apellido']
class ValidarUsuarioPrueba(validador.Schema):
    nombre = fields.Str()
    apellido = fields.Str()