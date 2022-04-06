from rest_framework import serializer
# https://www.django-rest-framework.org/api-guide/serializers/
# https://www.django-rest-framework.org/api-guide/fields/

class PruebaApiView(serializer.Serializer):
    # serializer => serialiaza la información aun formato definido
    nombre = serializer.CharField(max_length=40, trim_whitespace=True)
    apellido = serializer.CharField()
    correo = serializer.EmailField()
    dni = serializer.RegexField(max_length=8, min_length=8, regex="[0-9]")
    # dni = serializer.IntegerField(min_value=10000000, max_value=99999999)
