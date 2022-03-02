notas = [10, 20, 16, 8, 6,1]
for nota in notas:
    print (nota)

#Creamos un loop manual del 0 hasta el limite definido en el range()
for numero in range(10):
    print(numero)

#Creamo un loop manual con 2 paramentros el primero el inicio el segundo el limite
for numero in range(5,10):
    print(numero)

#Creamo un loop manual con 2 paramentros el primero el inicio el segundo el limite y el tercero es de cuanto en cuanto incrementara o decrementara
for numero in range(5,10,2):
    print(numero)

#imprimir los 3 valores iniciales de notas
for nota in notas[:3]:
    print(nota)

for posición in range(3):
    print(notas[posición])