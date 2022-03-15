from flask_restful import Resource, request
# all los metodos HTTP que vamos a utilizar se definen como metodo de la clase
class IngredientesCotroller(Resource):
    def get(self):
        return {
            'message': 'Yo soy el get de los Ingredientes'
        }
    
    def post(self):
        print(request.get_json())
        return {
            'message': 'Yo soy el post'
        }