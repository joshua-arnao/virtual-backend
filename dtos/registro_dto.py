#Validará que la información que venga sea correcta
from config import validador
from models.usuarios import Usuario

class RegistroDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario