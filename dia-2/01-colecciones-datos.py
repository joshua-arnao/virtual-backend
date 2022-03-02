#COLECCIONES DE DE DATOS ES UNA VARIABLE QUE PUEDE ALMACENAR VARIOS VALORES
#LIST(List)
#Ordenadas y que puede ser modificadas
nombre = ['Pedro', 'Luis', 'Danny', 'Cesar', 'Magaly']
combinada = ['Eduardo', 80, False, 15.8, [1, 2, 3]]

#Las listas inician en la posición 0
print(nombre[0])

#Cuando hacemos el uso de lo valores negativos de una lista internamente python le dará la vuelta a la lista
print(nombre[-1])

#Si ingresamos a una posición inexistente nos lanzara un error de 'indice fuera de rango
#print(nombre[10])

#pop() => remueve el último elemento de la lista y se puede alamacenar en otra variable
resultado = nombre.pop()
print(resultado)
print(nombre)

#append() => ingresa un nuevo elemento a la última posiciion de la lista
nombre.append('Juana')

#Elimina el contenido de la una posición de la lista pero no lo podemos almacenar en otra variables
del nombre[0]
print(nombre)

#clear() => limpia toda la lista y la deja como nueva
nombre.clear()
print(nombre)

x = combinada[:] #Es como el .copy pero ubica la lista en otro espacio de memoria
y = combinada

#Indica una sub seleccion de la lista
print(combinada[1:3]) #Traera desde la posición3

#Indicando el contenido de la lista y esto es muy útil para hacer la copia de la lista sin usar si mmisma posición de memoria
print(combinada[:])

print(id(x))
print(id(combinada))
print(id(y))

print(combinada[:2]) #desde el inicio hasta < 2
print(combinada[2:]) #desde la posición 2 hasta el final

meses_dscto = ['Enero', 'Marzo', 'Julio']
mes = 'Septiembre'
mes2 = 'Enero'

#Indicará si el valor principal no se encuentra dentro de la lista
print(mes not in meses_dscto)

#Indicará si el valor se encuentra en la lista
print(mes  in meses_dscto)

seccion_a = ['Roxana', 'Juan']
seccion_b = ['Julieta', 'Martin']

#Si hacemos una sumaroeia en las listas estas se combinaran en la cual la segunda lista ira despúes de la primera de la lista
print(seccion_a + seccion_b)

#Sirve para esperar un dato ingresado por el usuario
dato = input('Ingresa tu nombre:')
print(dato)

#TUPLAS
#Muy similar a las tuplas a excepcion que no se puede modificar
cursos = ('backend', 'frontend', 1, True)
print(cursos)
print(type(cursos))
print(cursos[0])

#Si dentro de una tupla hay una lista u otra colección de datos si se podra modificar esa sub colección
variada = (1,2,3, [4,5,6])
variada[3][0] = 'Hola' #Elemento 3 en la posición 0
print(variada)
print(type(variada))

#NOTA: La longitud siempre será la cantidad de elementos y esta siempre empezará en 1 mientras que la posición siempre empezarpa en 0, es por eso que la longitud es = posición -1
print(len(variada))

#CONJUNTOS(SET)
#Coleccion de datos DESORNEDA, una vez que se crea ya no se acceder a las posicionesde sus elementos
estaciones = {'Verano', 'Otonio', 'Primavera', 'Invierno'}
#Una vez que el conjunto se crea asignara una posición aleatoria pero no cambia cada vez que sea llamado el conjunto
print(estaciones)
estaciones.add('Otro')
estacion = estaciones.pop()
print(estacion)

#DICCIONARIOS
#Colección de datos DESORNEDA pero cada elemento obede a una llave difinida
persona = {
    'nombre': 'Joshua',
    'apellido': 'Arnao',
    'correo': 'joshua.arnao@icloud.com'
}
print(persona['apellido'])
print(persona.get('apellido', 'No hay no existe')) #el metodo get si no puede retornar informacion no dará un error

print(persona.keys()) #devuelve todas las llaves de mi diccionario
print(persona.values()) #devuelve el contenido de mi diccionario
print(persona.items()) #devuelve todas las llaves y sontenido en forma de tuplas

#Si definimos una llave que no existe, la creara, caso contrario modificaraá su valor
persona['edad'] = 28
persona['nombre'] = 'Ximena'
print(persona)

#NOTA: si la llave no es exactamente igual creara una nueva llave (tiene que coincidir minus y mayus)
persona['Nombre'] = 'Ximena'
print(persona)

#Eliminar una llave de un diccionario
persona.pop('apellido')
