 #*ERROR - es una mala ejecución del código y hará que deje de funcionar
#locals(['--builtins__']) => me retornara del diccionario de locals() todos los errores definidos en python
# dir => nos permite listar estos atributos como strings para poder leerlos facilmente
# locals() => nos devuelve todas las variables disponibles que tenemos en python en este scoope 
#print(dir(locals(['--builtins__'])))
try:
    valor = int(input('Ingresa un numero:'))
    print(valor) #ErrorValue
except ValueError:
    #Entrará a este excepr cuando el error sea de tipo ValueError
    print('Error al convertor un string a numero')
except Exception as error:
    print(error.args)
    #captura el error causante impidiendo que el programa deje de funcionar
    print('Ooops algo salio mal intentalo nuevamente')

print('Yo finalizo correctamente')

while True:
    try:
        valor = int(input('Ingresa un numero:'))
        break
    except:
        print('Valor incorrecto')

try:
    resultado = 1/1
except:
    print('Hubo un error')
else:
    #else en el caso que los try-except se ejecutara y nunca ingreso al except(condigo sin error)
    print('Yo soy el else')
finally:
    #Ingresara si el try fue exitoso o no osea si del mismo ingreso a algun except o no
    print('Yo me ejecutare si todo fue mal o fue bien')

productId = input('Ingresa el id del producto: ')
#iremos a la base de datos y buscaremos ese producto
# 1, 2, 3, 4, 5, 6, 7, 8, 9
try:
    if(productId == '10'):
        #emitira un error manualmente
        #se utilizara para no continuar con el flujo normal del proyecto
        raise Exception('El producto no existe en la bd')
except Exception as e:
    #ingresa si hubo error
    print('Ups algo salio mal en el producto a buscar, mensaje:',e.args[0])
else:
    #ingresa si no hubo error
    print('El producto econtrado es: ...')
finally:
    #ingresa si no hubo error
    print({'mensage':'Resultado final'})
