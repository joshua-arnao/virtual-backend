# from django.shortcuts import render => paara renderizar plantillas html
# https://www.django-rest-framework.org/ => convierte nuestro back para serconsumido por front
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request):
    # Request será toda la inforamción enviada por el cliente
    # https://www.django-rest-framework.org/api-guide/requests/
    print(request.method)
    print(request)
    if request.method == 'GET':
        # Comportamiento cuando sea GET
        return Response(data={
            'message': 'Bienevid@ a mi API de agenda'
        })
    elif request.method == 'POST':
        # Comportamiento cuando sea POST
        return Response(data={
            'message': 'Hiciste un post'
        }, status=201)

class PruebaApiView(ListAPIView):
    # serializer => serialiaza la información aun formato definido
    serializer = None
