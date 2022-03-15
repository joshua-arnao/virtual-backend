from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import IngredientesCotroller

app = Flask(__name__)
#Creamos la instancia de flask_restful.Api y le indicamos que toda la configuración que haremos se agrege a nuestra instancia de Flask
api = Api(app=app)

@app.route('/status', methods=['GET'])
def status():
    return{
        'status': True,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

#Ahora definimos las rutas que van a ser utilizadas con un determinado controlador
api.add_resource(IngredientesCotroller, '/ingredientes', '/ingrediente')

#comprobara que la intancia de la clase Flask se este ejecutnado en el archivo principal del proyecto, esto se usa para no crer multiples instancias y generar un posible error de Flask
if __name__ == '__main__':
    app.run(debug=True)

print('Hola')