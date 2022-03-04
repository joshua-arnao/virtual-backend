 #?OOP - Programación Orientada a objetos
 #La programación debe esta creada en base a clases
 #Toda parte del código debe ser tratada como una plantilla como si fuese una plantilla
 #clases => son plantillas para que puedan ser utilizadas varias veces sin la necesidad de modificar su formaa en relacion al objeto sino que al revez

class Person:
    #las variables creadas dentro de la clase pasan a llamarse atributos
    fec_nac = '2000-01-01'
    name = 'Juan'
    soltero = True
    estatura = 1.74
    #Las acciones que pueden tener una clase se definen como funciones, pero una funcion al ser creada dentro de una clase pasa a llamarse metodo
    #En cada metodo siempre como primer parametro obligatoriamente se utiliza la palabra self sirve para hacer referencia dentro de la instancia a los atributos y metodos de esa misma instancia para que haga uso de copia y que posiblemente no traiga la información estatica de la clase
    def saludar(self):
        self.decir_nombre()
        self.fec_nac
        print('Hola como estan')
        return 'Hola {}'.format(self.name)
         
    def decir_nombre(self):
        print('digo el nombre')

#Cuando una variable se crea a raiz de una clase, esta variable pasa a llamarse instancia (intancia => copia en su totalidad la clase)
person1= Person()
person2= Person()

#Modificamos el valor original del atributo a uno personalizado
person2.name = 'Eduardo'
person1.name = 'Carolina'

#Sobre escribimos el valor predeterminado del atributo nombre a una nueva y esta generá
print(person1.name)

Person.name = 'Robert'

print(person1.name)
print(Person.name)
