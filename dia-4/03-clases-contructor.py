class Animal:
    nombre = ''
    sexo = ''
    patas = 0
    #metodo constructor: este metodo se llamara cuando vayamos a crear una nueva instancia de la clase
    def __init__(self, nombre, sexo, nro_patas):
        #crear unos nuevos atributos dentro de la clase y estos ya no serás estaticos
        self.nombre = nombre
        self.sexo = sexo
        self.patas = nro_patas

    def description(self):
        #Si queremos que los atribtuos que vamos a utilizar sean creados puedan ser accedidos dessde cualquier parte de la instancia de la clase entonces los debemos de crear en el contructor
        return 'Yo soy un {}, soy {}, y tengo {} patas'.format(self.nombre, self.sexo, self.patas)
foca = Animal('Foca', 'M', 2)
caballo = Animal('Cabello', 'M', 4)
gato = Animal('Gato', 'F', 4)

print(foca.description())
print(caballo.description())
print(gato.description())
