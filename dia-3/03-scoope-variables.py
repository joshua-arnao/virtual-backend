nombre = 'Eduardo'

def saludar():
    #global => le indicamos a la funcion que queremos utilizar una variable definida fuera de la misma para hacer modificaciones
    global nombre
    print(nombre)

saludar()

#Definimos variable local
#si definimos las varibales dentro de la función solo se pueden usar dentro de las mismas
def venta():
    ganancia = 0.15

venta()
#no pododemos llamar una variable  local de una función
#print(ganancia)
