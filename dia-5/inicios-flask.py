 #!No se puede crear un aarchivo con el mismo nombre de una libreriía que camos a utilizar
from flask import Flask
from datetime import datetime

#__name__ => muestra si el archivo es el archivo principal del proyecto
app = Flask(__name__)
 #?diferencia de metodos y atributos

#Lo decoradores es un patron de software que se utiliza para modifcar el funcionamiento de un metodo o de una clase en particular sin la necesidad de emplear otros metodos como la herencia
@app.route('/')
def inicial():
    print("Me llamaron")
    #Siempre en los controladores tenemos que devolver una respuesta!
    return "Bienvenido a mi API 🔌"

@app.route('/api/info')
def info_App():
    return {
        #strftime => para darle formato a la fecha
        'fecha': datetime.now().strftime('%d-%m-%Y %H:%M:%S') #me devuelve la hora y fecha actual del servidor
    }
#inicializaremos nuestro servidor de Flask
#debugging => significa que estamos en un modo de prueba y con ello cada vez que guardemos se reiniara el servidor
app.run(debug=True)

#Tod lo lo que declaramos luego de la llamada al metodo run() nunca se ejecutara ya que el metodo run() hace que el programa espere la petición del cliente