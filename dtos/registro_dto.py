#Validará que la información que venga sea correcta
from config import validador
from models.usuarios import Usuario
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate, fields
# DTO => Data Transfer Object

class RegistroDTO(validador.SQLAlchemyAutoSchema):
    correo = auto_field(validate=validate.Email())
    class Meta:
        model = Usuario

class UsuarioResponseDTO(validador.SQLAlchemyAutoSchema):
    password = auto_field(load_only=True) # load_only => evitara que se muestre la contraseña
    class Meta:
        model = Usuario

class LoginDTO(validador.Schema):
    correo = fields.Email(required=True)
    password = fields.String(required=True)