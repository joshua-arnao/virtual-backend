#Esto es un comentario y sirve para dar contexto de que se hace, se hizo o se hará
#TODO: logica para este controlador para

#VARIABLE DE TEXTO
nombre = 'joshua'
apellido = 'arnao'

#Si queremos tener un texto que pueda contener saltos de línea
description = '''Hola amigos:
como están?'''

print(description)

#VARIABLE NUMERICAS
year = 2022

#type() => mostrará que tipo de varibale es
print(type(year)) #int: entero
print(type(description)) #str: string

#En python todas las variables deben de ser declaradas con su contenido
#None = null | undefined
especialidad = None #variable vacía 
print(type(especialidad)) #NoneType: vacía

mes, dia = 'febrero', 28
print(mes)

#del => elimina la variable de la memoria
del mes

print(mes) #is not defined