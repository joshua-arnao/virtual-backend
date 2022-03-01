#OPERADORES DE COMPARACIÓN
numero1, numero2 = 10, 20

#IGUAL QUE
print(numero1 == numero2)

#MAYOR QUE / MAYOR IGUAL QUE
print(numero1 > numero2)
print(numero1 >= numero2)

#MENOR QUE / MENOR IGUAL QUE
print(numero1 < numero2)
print(numero1 <= numero2)

#DIFERENTE DE
print(numero1 != numero2)

#OPERADORES LOGICOS
#Sirve para comparar varias comparaciones
#En JS se utiliza && pero en python se usa and
#En JS se utiliza || pero en python se usa or
print((10>5) and (10<20)) #Todas verdaderas - True
print((10>5) or (30<20)) #Almenos una considicion debe ser verdadera para que el resultado final sea verdadero


#OPERADORES DE IDENTIDAD
#Sirve para ver si estan apuntando a la misma dirección de memoria
#is
#iis not
verduras = ['apio', 'lechuga', 'zapallo']
verduras2 = verduras
verduras3 = ['apio', 'lechuga', 'zapallo']
#NOTA: las colecciones de datos son variables mutables(cuando cambio su contenido este se verá reflejado en todas las copias de dicha variable)
verduras2[0] = 'perejiel'
verduras2[1] = 'manzana'
#el metodo copy() copia todo el contenido de la variable pero se guardara en una nueva posición de la variable
verduras4= verduras.copy()
verduras4[0] = 'huacatay'
print(verduras2 is verduras) #true
print(verduras)
print(verduras2)
print(verduras3 is verduras) #false

print('la posicion de la variable versuras es:', id(verduras))
print('la posicion de la variable versuras es:', id(verduras2))
print('la posicion de la variable versuras es:', id(verduras4))

#Si hablamos de variables primitivas(str, int, float, boolean, date) entonces al hacer la copia compartira su mimso espacio de memoria pero al hacer alguna modificación a cualquiera de las 2 o mas variables que esten usando el mismo espacio de memoria automaticamente python le asignara uno nuevo 
nombre = 'joshua'
nombre2 = nombre
print(nombre2 is nombre) #true
print(id(nombre2))
print(id(nombre))
nombre2 = 'Carlos'
print(id(nombre2))
print(id(nombre))


nameUser = 'eduardo'
nacionalidad = 'cubano'
print(nameUser == 'eduardo' and (nacionalidad == 'peruano' or nacionalidad == 'colombiana'))