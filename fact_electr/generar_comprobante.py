from .models import Comprobante
from django.db import connection


def generar_comprobante(tipo_de_comprobante: int):
    tipo = ''
    opacion = 'generar_comprobante'
    if tipo_de_comprobante == 1:
        serie = 'FFF1'
    elif tipo_de_comprobante == 2:
        serie = 'BBB2'
    elif tipo_de_comprobante == 3 or tipo_de_comprobante == 4:
        serie = '0001'

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vista_prueba')
        print(cursor.fetchall())

    ultimoComprobante = Comprobante.objects.values_list('numero', 'serie').filter(
        tipo=tipo).order_by('-numero').first()

    # if not numero:
    if ultimoComprobante is None:
        numero = 1
    else:
        numero = int(ultimoComprobante[0]) + 1
