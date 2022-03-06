# para evitar el salto de linea en una impresion de pantalla print() podemos declarar un parametro end=''
print('hola',end='*')
print('estos son los ejercicios')
# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()

# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()

# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()

# height = int(input("Altura del rectangulo: "))
# width = int(input("Anchura del rectangulo: "))

# for h in range(height):
#     for w in range(width):
#         print("* ", end="")
#     print()

# widthOctogono = int(input("Anchura del octogono: "))

# for i in range(widthOctogono):
#     espacios = (widthOctogono-1) - i
#     print(' '*espacios + '*' * (i + 1)  + (widthOctogono - 2) * '*' + '*' *(i + 1))
# for h in range(widthOctogono - 2):
#     for w in range(widthOctogono):
#         if widthOctogono > 2:
            
#         print("*", end="")
#     print()


numero = int(input("Escribe un número entero positivo : "))

def functionCollatz(numero):
    print(numero)
    while numero != 1:
        if numero % 2:
            return functionCollatz(numero * 3 + 1)
        else:
            return functionCollatz(numero // 2)

if numero > 0:
    functionCollatz(numero)
else:
    print("El número no es válido")

