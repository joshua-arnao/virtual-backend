# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. En base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.

# class Person:
#     def __init__(self, name, fec_nac, nacionalidad, dni):
#         self.name = name
#         self.fec_nac = fec_nac
#         self.nacionalidad = nacionalidad
#         self.dni = dni

# class Alumno:
#     def __init__(self, name, cursos, dni):
#         super().__init__(name, dni)
#         self.cursos = cursos
#         self.__cusosMatriculados = self.cursos

# class Docente:
#     def __init__(self, seguroSocial, cts):
#         self.seguroSocial = seguroSocial
#         self.__cts = cts

class Persona:
    def __init__(self, nombre, fec_nac, dni, nacionalidad):
        self.nombre = nombre
        self.fec_nac = fec_nac
        self.nacionalidad = nacionalidad
        self.dni = dni

    def saludar(self):
        print("Hola, me llamo {}".format(self.nombre))


class Alumno(Persona):
    def __init__(self, nombre, fec_nac, dni, nacionalidad, cursos):
        super().__init__(nombre, fec_nac, dni, nacionalidad)
        self.__cursos = cursos


class Docente(Persona):
    def __init__(self, nombre, fec_nac, dni, seguro_social, nacionalidad, cts):
        super().__init__(nombre, fec_nac, dni, nacionalidad)
        self.cts = cts
        self.__seguro_social = seguro_social