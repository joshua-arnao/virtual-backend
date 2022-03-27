from sqlalchemy import Column, types, orm
from config import conexion
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey

class Movimientos(conexion.Model):
    __tablename__ = 'movimientos'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    monto = Column(type_=types.Float(), nullable=False)
    tipo = Column(type_=types.Enum('INGRESO', 'EGRESO'), nullable=False)
    descripcion = Column(type_=types.String(length=45))
    moneda = Column(type_=types.Enum('SOLES','DOLARES','EUROS'))
    fecha_creacion = Column(type_=types.DateTime(), default=datetime.datetime.now)

    #RELACIONES(fk con sus relatioships)
    # Llave foranea
    usuario_id = Column(ForeignKey(column='usuario_id', type_=types.Integer, nullable=False))
    #relationship - se usa backref para traer todos sus movimiento
    usuario = orm.relationship('Usuario', backref='usuario_movimiento')

    categoria_id = Column(ForeignKey(column='categoria_id', type_=types.Integer, nullable=False))
    categoria = orm.relationship('Categoria', backref='categoria_movimiento')