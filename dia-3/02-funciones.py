#FUNCION
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