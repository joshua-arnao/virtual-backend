#WHILE
number = 0
while number < 10:
    #pass => sirve para indicar dentro de un bloque de código que aún no hemos definido lógica
   print(number)
   number += 1
else:
    print('el while termino bien')


#En relación a los siguientes numeros indicar cuantos son pares y cuantos son impares
numeros =[1,5,16,28,234,67,29 ]

for numero in numeros:
    if numero % 2 == 0:
        print('El numero {} es par'.format(numero))
    else:
        print('El numero {} es impar'.format(numero))

par, impar = 0, 0
for numero in numeros:
    if numeros % 2 == 0:
        par +1
    else:
        impar +=1

print('Hay {} numero pares'.format(par))
print('Hay {} numero impares'.format(impar))

posicion = 0
par, impar = 0, 0
while posicion < len(numeros):
    if numeros[posicion] % 2 == 0:
        par +=1
    else:
        impar += 1
    posicion += 1

print('Hay {} numero pares'.format(par))
print('Hay {} numero impares'.format(impar))
