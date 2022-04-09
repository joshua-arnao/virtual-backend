from calendar import c
from pyexpat import model
from rest_framework import serializers
from .models import Tareas, Etiqueta
# https://www.django-rest-framework.org/api-guide/serializers/
# https://www.django-rest-framework.org/api-guide/fields/

class PruebaSerializer(serializers.Serializer):
    # serializer => serialiaza la información aun formato definido
    nombre = serializers.CharField(max_length=40, trim_whitespace=True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length=8, min_length=8, regex="[0-9]")
    # dni = serializers.IntegerField(min_value=10000000, max_value=99999999)


# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
# ModelSerializer => se utiliza para poder usar los modelos ya que generará todos los fields 
class TareasSerializer(serializers.ModelSerializer):
    # Modifico la configuración del modelo y le puede setear la nueva configuración que respetara el serializador, no se pude hacer cambios de tipode de datos drasticos (por ejemplo: si el modelo es un InterField en el serializador no podre cambiarlo a CharField porque me lanzará un error al moemtno de guardar la data)
    foto = serializers.CharField(max_length=100)
    class Meta:
        model = Tareas
        fields = '__all__' # Usaremos todas las columnas de mi table
        # exclude = [] # Indicara que columna no se se utilizará
        # NOTA: No se pueden utilizar las 2 a la vez es decir o se usa fields o el exclude
        #depth = 1 # Sirve para que en el caso que querramos devolver la informacion de una relacion entre este modelo podemos indicar hasta que grado de profundidad queremos que nos devuelva la informacion, la profundida maxima es de 10
        extra_kwargs = {
            'etiquetas': {
                'write_only': True
            }
        }
        # La profundida solamente funcionara cuando een el modelo en la cual lo estemos utilizando sea el model en el cual se encuentra la realación como atributo

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        depth = 1

class EtiquetaSerializer(serializers.ModelSerializer):
    # Inidicare que este atributo solamente funcionara para cuado vamos a serializar la data antes de devolverla mas mp ára ciamdp querramos usarla para escritura
    # Se tiene que llamar igual que el rellated_name para poder ingresara a esa relación o podremos definir el parametro source en el cual colocaremos el nombre del related_name
    # NOTA: No podemos utilizat el parametro source si es que tambien colocaremos el mismo valor como nombre del atributo
    tareas = TareasSerializer(many=True, read_only=True)
    # no_es_tareas = TareaSerializer(many=True, read_only=True, source='tareas')
    class Meta:
        model= Etiqueta
        fields = '__all__'
        # ¿Cómo puedo mediante un serializador indicar que columnas de determinado modelo serán solamente escritra o solamente lectura sin modificar su comportamiento como un atributo de la clase?
        # extra_kwargs y read_only_fields solamente funcionaraán para cuando nosotros querramos modificar el comportamiento de los atributos que no los hemos modficado manualmente dentro del serializador
        extra_kwargs = {
            'nombre': {
                'write_only': True
                },
            'id':{
                'read_only': True
                }
        }
        # Los campos del modelo que solamente quiero que sean lectura los podre definir en una lista
        read_only_fields = ['createdAt']


class TareaPersonalizableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        # Exclude = ['nombre] # funciona tanto para lectura como escritura
        extra_kwargs = {
            'nombre': {
                'read_only': True
            }
        }

class ArchivoSerializer(serializers.Serializer):
    archivo = serializers.ImageField(max_length=100, use_url=True)