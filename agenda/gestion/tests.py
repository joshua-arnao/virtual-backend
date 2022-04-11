from django.test import TestCase
from rest_framework.test import APITestCase
# APITestCase => Esta clase sirve para hacer caso de test como un unittest

# Create your tests here.
class EtiquetasTestCase(APITestCase):
    def test_crear_etiqueta_success(self):
        # Hago la petición a mi backend con cierta data a mi body
        request = self.client.post('/gestion/etiquetas', data={
            'nombre': 'Frontend'
        })
        print(request.data)
        self.assertEqual(request.status_code, 201)
        # assertEqual => Afirmamos que el primer parametro es igual al segungo
        self.assertEqual(1, 1)
