#Crea una clase Alumno con los atributos privados nombre y notas (una lista de números).
class Alumno:

    '''El constructor debe permitir inicializar el nombre y, opcionalmente, una lista de
        notas (vacía por defecto)'''
    def __init__(self, nombre, notas):
        self.__nombre = nombre
        self.__notas = []

        # Comprobar que se pasan notas, no se puede agregar un alumno sin notas
        if not notas:  # notas es None o lista vacía
            raise ValueError("El alumno debe tener al menos una nota inicial")

        # comprobar que las notas estan entre 0 y 10 y agregarlas a la lista
        for nota in notas:
            if nota < 0 or nota > 10:
                raise ValueError(f"La nota {nota} no está entre 0 y 10")
            self.__notas.append(nota)

    #GETTER Y SETTER
    @property
    def nombre(self):
        return self.__nombre

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas):
        self.__notas = notas

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


    '''Implementa un método agregar_nota(nota) que añada una nota a la lista,
    lanzando una excepción si la nota no está entre 0 y 10'''

    def agregar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        self.__notas.append(nota)

    '''Implementa un método media() que devuelva la nota media del alumno. Si la lista
    está vacía, lanza una excepción.'''
    def calcular_media(self):
        if len(self.__notas) == 0:
            raise ValueError("La lista de notas está vacía")
        media= sum(self.__notas) / len(self.__notas)
        return media

if __name__ == "__main__":

    #Crea varios dos listas de alumnos, uno con datos correctos y otro con algunos datos incorrectos, que maneje las excepciones con try/except
    lista=[]

    alumnos=[
    ("Juan", [1, 7, 9]),
    ("Maria", [8, 4, 7]),
    ("Pedro", [-1, 5, 6]),
    ("Ana", [10, 9, 11]),
    ("Luis", None)
    ]
    for nombre, notas in alumnos:
        try:
            alumno=Alumno(nombre, notas)
            lista.append(alumno)
        except ValueError as e:
            print(f"Error al crear el alumno {nombre}: {e}")

    #Muestra la media de cada alumno antes y despues de añadir una nota, manejando las excepciones
    # Mostrar notas y media final después de agregar una nota
    for alumno in lista:
        try:
            print(f"\nAlumno: {alumno.nombre}")
            print(f"Notas iniciales: {alumno.notas}")

            # Agregar una nota extra
            alumno.agregar_nota(7)
            print(f"Notas después de agregar 7: {alumno.notas}")

            # Calcular media final
            media = alumno.calcular_media()
            print(f"Media final: {media:.2f}")# esto permite mostrar dos decimales

        except ValueError as e:
            print(f"Error con el alumno {alumno.nombre}: {e}")






