#factory
from faker import Faker
from faker.providers import internet, person, phone_number

fake = Faker()
#Le agregamos un provider adicional a nuestro faker para que ahora pueda utilizar los tradicionesles y lo de interet
#fake.add_provider({internet, phone_number, person})
#tanto el add_provider como el provider es necesario declararlo siempre que se este usando un standard provider (solamente sra necesario cuando sea un provider de la comunidad)

for persona in range(100):
    nombre = fake.first_name()
    apePat = fake.last_name()
    appeMate = fake.last_name()
    correo = fake.ascii_free_email()
    telefono = fake.bothify(text='9########')
    sql = '''INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES 
                                ('%s', '%s', '%s', '%s', '%s');''' % (nombre, apePat, appeMate, correo, telefono)
    #En otras versiones 
    #sql2 = '''INSERT INTO alumnos (nombre, apellido_paterno, correo, numero_emergencia) VALUES 
    #                            ({}, {}, {}, {}, {});'''.format(nombre, apePat, appeMate, correo, telefono)
    #--print(sql)

def generar_niveles():
    secciones = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer Piso', 'Segundo Piso', 'Tercer Piso']
    niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto' 'Quinto', 'Sexto']

    for nivel in niveles:
        pos_secciones = fake.random_int(min=1, max=3) #Entre 0 hasta <= 2 (0|1|2)
        for posicion in range (0, pos_secciones):
            pos_ubicacion = fake.random_int(min=0, max=3)
            seccion = secciones[posicion]
            ubicacion = ubicaciones[pos_ubicacion]
            nombre = nivel
            sql = '''INSERT INTO niveles (seccion, ubicacion, nombre) VALUES
                                        ('%s', '%s', '%s');''' % (seccion, ubicacion, nombre)
            # print('Nivel', nivel)
            # print('Sección', secciones[posicion])
            # print('Ubicación', ubicaciones[pos_ubicacion])
            print(sql)

generar_niveles()

