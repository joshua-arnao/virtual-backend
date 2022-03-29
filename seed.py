#cuando se ejecute este archivo se alimentara la base de datos
from models.categorias import Categoria
from config import conexion
from sqlalchemy import or_

#Leer en la base dedatos si no existen las categorias: 'OCIO', 'COMIDA, 'EDUACION' Y 'VIAJES'
def categoriasSeed():
    #Si no existe las categorías ya no se ingresa
    conexion.session.query(Categoria).filter(
        or_(Categoria.nombre == 'OCIO', Categoria.nombre == 'COMIDA')
        ).first()
    pass