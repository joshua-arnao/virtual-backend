from config import validador
from models.ingredientes import Ingrediente

class IngredienteRequestDTO(validador.SQLAlchemyAutoSchema):
    #Al heredar de SQLAlchemyAutoSchema estamos indicando que usaremos un modelo como mapeo de los atributos necesarios para hacer la validación de nuestra informacion para
    class Meta:
        model = Ingrediente