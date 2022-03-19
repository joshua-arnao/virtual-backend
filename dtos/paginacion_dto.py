from config import validador
from marshmallow import fields

class PaginacionRequestDTO(validador.Schema):
    #load_default => sirve para que en el caso no tenga valor esa variable entonces su valor por defecto a la hora de hacer el load (cargar) será el indicado, NOTA: tiene que ser el mismo tipo de dato que hemos definifo
    page = fields.Integer(required=False, load_default=1)
    perPage = fields.Integer(required=False, load_default=10)