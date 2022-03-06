 #*HERENCIA => extraer información de un clase padre
#DRY => Don't repeat yourself
class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def saludar(self):
        return 'hola soy {}'.format(self.nombre)

class Alumno(Usuario):
    def __init__(self, nombre, apellido, correo, padres):
        #super() => sirve para mandar a llamar a la clase de la cual estamos haciendo herencia para no volver a escribir de la misma lógica
        super().__init__(nombre, apellido, correo)
        self.padres = padres

    def info(self):
        #El metodo super solo servira para poder acceder a los metodos de la clase de la cual estamos heredando
        return {
            'nombre':self.nombre,
            'apellidos':self.apellido,
            'padres': self.padres,
            'saludar': super().saludar()
        }

alumnoPedro = Alumno('Pedro', 'Flores', 'pflores@gmail.com', [{
    'nombre': 'Wilbert',
    'apellido': 'Martniez'
}, {
    'nombre': 'Juliana',
    'apellido': 'Perez'
}])

print(alumnoPedro.info())