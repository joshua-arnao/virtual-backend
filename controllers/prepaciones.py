import re
from flask_restful import Resource, request
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionRequestDTO

class PrepacionesController(Resource):
    def post(self):
        try:
            body = request.get_jason()
            data = PreparacionRequestDTO().load(body)
            print(data)

            return {
                'message': 'Preparacion CREADA EXITOSAMENTE'
            }, 201

        except Exception as e:
            return{
                'message': 'Hubo un error al crear la preparacion',
                'content': e.args
            }, 400
            
