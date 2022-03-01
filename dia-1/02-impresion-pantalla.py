nombre = 'joshua'
print(nombre)

#concatenar varios valores
print('el nombre:', nombre, 'del usuario')

#El metodo format se utiliza {} con la cantidad de variables
estadoCivil = 'viudo'
print('La persona {} es {}'.format(nombre, estadoCivil))

#ademas podemos agregar la posicion de la variable que queremos imprimir
print('{1} es una persona {0}'.format(estadoCivil, nombre))