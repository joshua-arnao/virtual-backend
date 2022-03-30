from config import validador
from marshmallow import fields

#para validar que sea un correo
class ResetPasswordRequestDTO(validador.Schema):
    correo = fields.Email()