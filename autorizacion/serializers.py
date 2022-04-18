from rest_framework import serializers
from .models import Usuario


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    def save(self):
        # creo una instancia de mi usuario con los campos ya validados (validated_data)
        # ** => Pasar lo datos de un diccionario a parametros
        nuevoUsuario = Usuario(**self.validated_data)

        # encripto la password
        nuevoUsuario.set_password(self.validated_data.get('password'))

        # guardo el usuario en la bd
        nuevoUsuario.save()

        return nuevoUsuario

    class Meta:
        model = Usuario
        exclude = ['groups', 'user_permissions']
        # fields = '__all__'
        # Mediante el atibuto extra_kwargs indicar que la password será de solo escributira y ademas que el is sea solo selecuta
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'id': {
                'read_only': True
            }
        }
