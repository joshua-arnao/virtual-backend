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

aprobados = ['Eduardo', 'Pedro', 'Maria', 'Fatima']

for aprobado in aprobados:
    if(aprobado == 'Pedro'):
        print('El aprobado esta aprobado')
        break #Generá que el loop se detenga de manera abupta
else:
    print('Termino de ejecutarse el for de manera normal') # else se ejecuto despues de haber iterado el loop for

print('Termino de ejecutarse el for')

#----------------------------------------------------------------
products = ['manzanas', 'peras', 'Tallarines', 'Tazas']
search = input('Ingrese el producto a buscar: ')

for product in products:
    if product == search:
        print('El producto si esta en la tienda')
        break
else:
    print('No se encontro el producto a buscar')

print('igual yo me ejecuto')