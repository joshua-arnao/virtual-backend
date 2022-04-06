from tkinter.messagebox import CANCEL
from turtle import update
from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    # Tipo de columnas => https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    # Opciones de las columnas => https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=20, unique=True, null=False)
    # Columnas de auditoria para
    # Son columnas que podrán ayudar al segumineto de la creación de registros
    # createdAt => Es la fecha en la cual se creo el registro
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_et')
    # updatedAt => Es la fecha en la cual se modifico algún campo del registro
    updateAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    # Todas las configuraciones propias de la tabla se harán mediante la definición de sus atributos en la clase Meta
    # https://docs.djangoproject.com/en/4.0/ref/models/options/
    class Meta:
        # Cambiar el nombre de la tabla en la bd ( a diferencia del nombre de la clase)
        db_table = 'etiquetas'
        # Modificar eñ ordenamiento natural (por el id) e imponiendo el propioo que sea ASC del nombre, solamente funcionara para cuando hagamos el get usando el ORM
        ordering = ['-nombre']

class Tareas(models.Model):

    class CategoriasOpciones(models.TextChoices):
        TODO = 'TODO', 'TO_DO'
        IN_PROGRESS= 'IP', 'IN_PROGESS'
        DONE= 'DONE', 'DONE'
        CANCELLED = 'CANCELLED', 'CANCELLED'

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    categoria = models.CharField(max_length=45, choices=CategoriasOpciones.choices, default=CategoriasOpciones.TODO)

    # Forma 2 usando una lista de tuplas
    # categoria = models.CharField(max_length=45, choices=[
    # ('TODO, 'TO_DO').
    # ('IP', 'IN_PROGESS')
    # ('DONE', 'DONE')
    # (CANCELLED, 'CANCELLED')
    # ], default='TODO)

    fechaCaducidad = models.DateTimeField(db_column='fecha_caducidad')
    importancia = models.IntegerField(null=False)
    descripcion = models.TextField()

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_et')
    updateAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    # En Django se puede utilizar las relaciones one-to-one, one-to-many o many-to-many para crear las relaciones entre las tablas, aca ya no es necesario usar las relationships porque ya están integradas dentro de la relación
    etiquetas = models.ManyToManyField(to=Etiqueta, related_name='tareas')
    class Meta:
        db_table = 'tareas'

# si la tabla tareas_etiqueta no fuese una tabla pivote, detalle entonces tendria que crear la tabla como si fuese una tabla común y corrientes
# class TareasEtiquetas(models.Model):
#     etiquetaFK = models.ForeignKey(to=Etiqueta)
#     tareaFK = models.ForeignKey(to=Tareas)
#     #las demas columnas


