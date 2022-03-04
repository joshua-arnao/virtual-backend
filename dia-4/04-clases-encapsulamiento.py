 #*ENCAPSULAMIENTO - Es declaar tipo de accesibilidad a los atributos y metodos
class Producto:
    def __init__(self, nombre, precio):
        #Exiten 3 tipos de accesibilidad a los atributos y metodos de una clase: public
        self.nombre = nombre
        self.precio = precio
        #privado: cuando se define un atibuto con '__' estarmemos indicando que será privado y que no podra ser accedido desde fuera de la clase ni siquiera su misma instancia podrá acceder
        #un atributo sera cuando no es necesaria la intercción con un agente externo
        self.__ganancia = self.precio * 0.30
        #protegido protected

    def mostrar_info(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'ganancia': self.__ganancia,
            #{:.2f}.format() se convieerte el valor a string y redondeara el resultado
            'igv': '{:.2f}'.format(self.__calcular_igv(),)
        }

    def aumentar_ganancia(self):
        self.__ganancia = self.__ganancia * 1.10

    def __calcular_igv(self):
        resultado = self.precio * 0.18
        return resultado

cepillo = Producto('Cepillo dental', 3.80)
#atributo publico = porque puedo acceder a este tanto desde la misma clase como en su instancia
cepillo.nombre
#atributo privado = solamente podrá ser accesido a el dentro de la misma clase pero no desde su instancia de
cepillo.__ganancia = 100

print(cepillo.mostrar_info())
cepillo.aumentar_ganancia()
print(cepillo.mostrar_info())