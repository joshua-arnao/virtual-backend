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
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__' # Usaremos todas las columnas de mi table
        # exclude = [] # Indicara que columna no se se utilizará
        # NOTA: No se pueden utilizar las 2 a la vez es decir o se usa fields o el exclude

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Etiqueta
        fields = '__all__'