#FUNCIONES
#Almacenara un bloque de codigo con su comportamiento y solamente se ejecutran cuando estas son llamadas
def sumar(numero1, numero2):
    print('Se realizará la sumatoria ...')
    print(numero1 + numero2)

sumar(5, 2)

def nombre(x):
    '''Funcion que recibe un string y lo imprime por consola :)'''
    print(x)

nombre('Eduardo')
#mostrara la domuentación de la función si es que hay
print(nombre.__doc__)

user = []
def register(name, email, phone):
    '''Función que registra un usuario y lo guarda en una lista'''
    user.append({
        'name': name,
        'email': email,
        'phone': phone
    })
    return {
        'message': 'Registrado exitosamente',
        'user': user
    },True, 1

resultado, estadoCivil, nacionalidad = register('Joshua', 'joshua@email.com', '993777888')
print(resultado)
print(estadoCivil)
print(nacionalidad)


#Si creamos una funcion que reciba paramentros. estos parametro son opcionales SIEMPRE deben ir al final, primero son los requeridos y luego los opcionales
products = []

def register_products(name, price, state=True, stock='Almacen de cercado'):
    products.append({
        'name': name,
        'price': price,
        'state': state,
        'stock': stock
    })
    return 'Producto agregado exitosamente'

#Siempre debemos pasar obligatoriamente los parametros que no tienen los valores por defecto
register_products('Tomates', 4.50)
register_products('Apio', 1.40, False)
register_products('Cebolla', 5.30, True, 'Almacen nuevo mercado')
#otra forma de pasar paramentros
register_products(stock='Almacen de la costa', name='Pescado tilapia', price=2.5)



def alumnos(*args):
    print(args)

alumnos('eduado', 'nahia', 'Mario', 'Gean Carlo')
alumnos('eduado', 'roxana', 'Luis', 'Pedro')
alumnos('juanito')
alumnos('martha', 20, False, 'Juan', 1.5)

#kwrags => keyword arguments
#Si la función queremos recibir numero ilimiado de argumentos usaremos los kwargs y estos se alcenaran en el diccionario
def ingresarProducto(**kwargs):
    print(kwargs)
    if(kwargs.get('nombre')):
        print('El usuario quiere agregar un producto con el nombre')
    if(kwargs.get('cantidad')):
        print('El usuario quiere ingresar la cantidad del producto')

ingresarProducto(nombre = 'manzana', precio = 2.4, estado = True, pais_procedencia = 'Perú')
ingresarProducto(tamanio = 'Grande', cantidad=100, nombre='Pera de agua')

#*RECURSIVIDAD
#Es utilizar la función dentro de la misma función de la cantidad
def saludar_n_veces(limite):
    if(limite == 0):
        return 'Llegue al limite'
    print('Saludar')
    return saludar_n_veces(limite-1)

resultado = saludar_n_veces(10)

print(resultado)


# def factorial(number):
#     if number==0 or number==1:
#         resultado = 1
#     elif number > 1:
#         resultado = number*factorial(number-1)
#     return resultado

# respuesta =  factorial(5)
# print(respuesta)

def factorial(limite):
    if limite == 0:
        return 1
    return limite * factorial(limite - 1)

resultado = factorial(1)
print(resultado)
# ventajas:
# hace el codigo mas limpio y sin mucha duplicidad del mismo
#una tarea compleja se puede dividir en si misma de una manera mas facil y sencilla
#la generacion de subsecuencias es mas facil con la recursividad que con alguna iteracion anidada (while)

# desventajas:
#a veces la logica para genera una funcion recursiva es dificil de seguir
#las llamas recursivas son mas costosas ya que ocupan mas memoria por el simple echo de volver a llamar a toda la funcion de nuevo dentro de si misma y obviamente esto generara un mayor tiempo de respuesta
#las funciones recursivas son dificiles de hace depuracion (seguimiento al codigo linea x linea)****

#*OPERADOR TERNARIO

nombrePersona = 'Maria'
origenPersona = 'Cuzco'
desicion = 'Me caso' if nombrePersona == 'Maria' and origenPersona == 'arequipa' else 'next'
print(desicion)

#*LAMDA FUNCTION
#Son fuciones que puede tener un numero indeterminado de argumentos pero solamente una expresión(una sola línea de ejecución de codigo) ademas sera retornada para

cuadrado = lambda numero: numero ** 2
sacar_igv = lambda precio: precio * 0.18

rpta = cuadrado(4)

precio_sin_igv = sacar_igv(100)
print(rpta)
print(precio_sin_igv)

precio_sin_igv = sacar_igv(50)
print(precio_sin_igv)
