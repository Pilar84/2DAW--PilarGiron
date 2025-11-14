#Crea una clase Libro con los atributos privados titulo, autor y prestado (booleano).
'''Define el constructor y un método prestar() que cambie el estado a True.
o Si el libro ya está prestado, lanza una excepción'''
class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__prestado = False

    def prestar(self):
        if self.__prestado:
            raise Exception("El libro ya está prestado.")
        else:
            self.__prestado = True

    '''Define un método devolver() que lo marque como no prestado.
    o Si ya está disponible, lanza una excepción.'''
    def devolver(self):
        if not self.__prestado:
            raise Exception("El libro ya está disponible.")
        else:
            self.__prestado = False

'''Implementa una clase Biblioteca que mantenga una lista de objetos Libro.
o Añade métodos agregar_libro(libro), buscar_por_titulo(titulo) y
mostrar_libros().'''
class Biblioteca:
    #lista de objeta Libros vacia inicialmente
    def __init__(self):
        self.__libros = []

    #agregar libro a la lista
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    #recorremos la lista libros buscando el titulo y devolvemos el libro si lo encontramos
    def buscar_por_titulo(self, titulo):
        for libro in self.__libros:
            if libro._Libro__titulo == titulo:
                return libro
        return None
    #
    def mostrar_libros(self):
        #recorremos la lista de libros y mostramos su estado
        for libro in self.__libros:
            if libro._Libro__prestado:
                estado = "Prestado"
            else:
                estado = "Disponible"        
            print(f"Título: {libro._Libro__titulo}, Autor: {libro._Libro__autor}, Estado: {estado}")


if __name__ == "__main__":

    '''Crea un bloque main que simule el préstamo y devolución de varios libros, usando
    try/except/finally donde sea necesario.'''
    #creamos objeto biblioteca
    biblioteca = Biblioteca()
    #creamos una lista de libros
    libros=[
        ("El Quijote", "Miguel de Cervantes"),
        ("Cien Años de Soledad", "Gabriel García Márquez"),
        ("1984", "George Orwell"),
        ("Cien Años de Soledad", "Gabriel García Márquez"),
        ("El Quijote", "Miguel de Cervantes"),
    ]

  
    #Intentamos agregar los libros a la biblioteca manejando las excepciones
     # Agregar libros a la biblioteca
    for titulo, autor in libros:
        try:
            libro = Libro(titulo, autor)
            biblioteca.agregar_libro(libro)  # Usar el método correcto
        except Exception as e:
            print(f"Error al añadir el libro {titulo}: {e}")
   
    # Mostrar estado inicial
    print("\nEstado inicial de la biblioteca:")
    biblioteca.mostrar_libros()
    print("---------------")

    # Simular préstamo de un libro
    try:
        libro_a_prestar = biblioteca.buscar_por_titulo("1984")
        if libro_a_prestar:
            libro_a_prestar.prestar()
            print(f"\nHas prestado el libro: {libro_a_prestar._Libro__titulo}")
        else:
            print("El libro no se encontró en la biblioteca.")

        # Intentar prestar de nuevo para provocar excepción
        libro_a_prestar.prestar()
    except Exception as e:
        print(f"Error al prestar el libro: {e}")
        print("---------------")
    finally:
        # Mostrar estado después del préstamo, vemos que el estado del libro 1984 ha cambiado a prestado
        print("\nEstado de la biblioteca después del préstamo:")
        biblioteca.mostrar_libros()
    print("---------------")

    # Simular devolución de un libro
    try:
        libro_a_devolver = biblioteca.buscar_por_titulo("1984")
        if libro_a_devolver:
            libro_a_devolver.devolver()
            print(f"\nHas devuelto el libro: {libro_a_devolver._Libro__titulo}")
        else:
            print("El libro no se encontró en la biblioteca.")

        # Intentar devolver de nuevo para provocar excepción
        libro_a_devolver.devolver()
    except Exception as e:
        print(f"Error al devolver el libro: {e}")
        print("---------------")

    finally:
        # Mostrar estado final, observamos que al devolver el libro el estado ha cambiado a disponible de nuevo
        print("\nEstado final de la biblioteca:")
        biblioteca.mostrar_libros()
        print()

    




