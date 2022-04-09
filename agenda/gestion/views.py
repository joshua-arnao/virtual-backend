# from django.shortcuts import render => paara renderizar plantillas html
# https://www.django-rest-framework.org/ => convierte nuestro back para serconsumido por front
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import ( PruebaSerializer, 
                           TareasSerializer,
                           EtiquetaSerializer,
                           TareaSerializer,
                           TareaPersonalizableSerializer,
                           ArchivoSerializer)
from .models import Tareas, Etiqueta
from rest_framework import status
# Son un conjunto de librerias que django nos proveee para poder utilizar de una manera más rapida ciertas configuraciones
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# GET => DEVOLVER, POST => CREAR, PUT => ACTUALIZAR, DELETE => ELIMINAR, PATCH => ACTUALIZACIÓN PARCIAL
# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request ):
    # Request será toda la inforamción enviada por el cliente
    # https://www.django-rest-framework.org/api-guide/requests/
    print(request.method)
    print(request)
    if request.method == 'GET':
        # comportamiento cuando sea GET
        return Response(data={
            'message': 'Bienvenido a mi API de agenda'
        })

    elif request.method == 'POST':
        # comportamiento cuando sea POST
        return Response(data={
            'message': 'Hiciste un post'
        }, status=201)

class PruebaApiView(ListAPIView):
    # Sirve para ayudarnos a cuando se llame este request nos haga el trabajo de serializar y desealizar la inforamción (es igual que un DTO)
    # serializer => serialiaza la información aun formato definido
    serializer_class = PruebaSerializer
    # queryset => encargado de hacer la búsqueda para este controlador (para todos sus metodos)
    queryset = [{
        'nombre':'Joshua', 
        'apellido': 'Arnao', 
        'correo':'joshua@gmail.com',
        'dni':'74123050', 
        'estado_civil':'viudo'},
        {
        'nombre':'Karla', 
        'apellido': 'Lozano', 
        'correo':'joshua@gmail.com',
        'dni':'74123050', 
        'estado_civil':'viudo'}]

    def get(self, request: Request):
        # Dentro de las vistas genericas se puede sobrescribir la lógica incial del controlador
        # Si modifico la lógica original de cualquier generico en base a su metodo a utilizar ya no será necesario definir los atributos serializer_class y queryset ya que estos no se usan para cuando se modifica la lógica original
        informacion = self.queryset
        # Uso el serializador para filtrar la información necesaria y no mostrar información demas pero en este caso como le voy a pasar uno o mas registros de usuario entonces para el serializador los pueda iterar le coloco el parametro many=True que lo que hará será iterar
        informacion_serializada = self.serializer_class(data=informacion, many=True)
        # Para utilizar la informacion serializada OBLIGATORIAMENTE tengo que llamar al metodo is_valid() el cual internamente hara la validacion de los campos y sus configuraciones
        # raise_exception=True => Este parametro hara la emision del error si que hay indicado cual es el error
        informacion_serializada.is_valid(raise_exception=True)
        return Response(data={
            'menssage':'Hola', 'content':informacion_serializada.data
            })


class TareasApiView(ListCreateAPIView):
    queryset = Tareas.objects.all() # SELECT * FROM Tareas;
    serializer_class = TareasSerializer

    # https://www.django-rest-framework.org/api-guide/status-codes/#status-codes
    def post(self, request: Request):
        # Serializo la data para validar sus valores y su configuración
        serializador = self.serializer_class(data=request.data)
        if serializador.is_valid():
            # serializador.initial_data => Data inicial sin la validación
            # Serializador.validated_data => Data ya validada (Solo se puede llamar luego de llamar al metodo is_valid())
            fechaCaducidad = serializador.validated_data.get('fechaCaducidad')
            print(type(serializador.validated_data.get('fechaCaducidad')))
            importancia = serializador.validated_data.get('importancia')

            if importancia < 0 or importancia > 10:
                return Response(data={
                    'message': 'La importancia debe de ser entre 0 y 10'
                }, status=status.HTTP_400_BAD_REQUEST)

            if timezone.now() > fechaCaducidad:
                return Response(data={
                    'message': 'La fecha no puede ser menor que la fecha actual'
                }, status=status.HTTP_400_BAD_REQUEST)
            # El metodo save() se podra llamar siempre que el serializado sea un ModelSerializer y este servira para poder guardar la información actual del serializado en la bd
            serializador.save()

            return Response(data=serializador.data, status=status.HTTP_201_CREATED) # Created
        else:
            # Mostrará todos los errores que hicieron que el is_valid() no cumpla la conidción
            # serializador.errors 
            return Response(data={
                'message': 'La data no es valida',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer


class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer
    queryset = Tareas.objects.all()

class ArchivosAPIView(CreateAPIView):
    serializer_class = ArchivoSerializer

    def post(self, request:Request):
        print(request.FILES)

        queryParams = request.query_params
        carpetaDestino = queryParams.get('carpeta')

        data = self.serializer_class(data=request.FILES)
        if data.is_valid():
            print(data.validated_data.get('archivo',))
            # https://docs.djangoproject.com/es/4.0/_modules/django/core/files/uploadedfile/
            archivo: InMemoryUploadedFile = data.validated_data.get('archivo')
            print(archivo.size)
            print(archivo.name)

            if archivo.size > (5 * 1024 * 1024):
                return Response(data={
                    'message':'Archivo muy grande, no puede ser mas de 5mb'
                }, status=status.HTTP_400_BAD_REQUEST)
                
            # https://docs.djangoproject.com/en/4.0/topics/files/#storage-objects
            # El metodo read( sirve par leer el archivo Pero la lectura hará que tambien se elimine de la memoria temporal por ende no se puede llamar dos o mas veces a este método ua que la segunda ya no tendremos archivo que mostrar)
            resultado = default_storage.save(
                (carpetaDestino+'/' if carpetaDestino is not None else '') + archivo.name, ContentFile(archivo.read()))
            print(resultado)

            return Response(data={
                'message':'archivo guardo exitosamente',
                'content':{
                    'ubicación': resultado
                }
            },
            status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al subir la imagen',
                'content': data.errors
                },status=status.HTTP_400_BAD_REQUEST)
        
       



