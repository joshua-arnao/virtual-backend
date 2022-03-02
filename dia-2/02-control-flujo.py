#CONTROL DE FLUJO
#IF - ELSE
edad = int(input('Ingresa tu edad:'))
if (edad >= 18 ) :
    print('La persona es mayor de edad')
    print('otra impresion')
elif edad > 15:
    print('Puedes ingresar a la preparatoria')
else:
    print('Eres menor de edad')

print('finalizo el programa')

#Validar si un numero(ingresos de una persona) ingresado por teclado es:
#mayor a 500: indicar no recibe bono yanapai 
#entre 500

ingresos = int(input('Indica cual es tu ingreso mensual:'))
if (ingresos > 500):
    print('No recibe bono yanapai')
elif(ingresos >= 250):
    print('Si recibe bono Yanapai')
else:
    print('Si recibe bono Yanapai y balon de gas')
