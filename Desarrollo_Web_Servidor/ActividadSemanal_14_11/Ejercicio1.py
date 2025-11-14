#creamos la clase producto
class Producto:
    '''Implementa el constructor para inicializar los atributos. Si el precio o el stock son
    negativos, lanza una excepción ValueError con un mensaje adecuado.'''


    #atributos privados
    def __init__(self, nombre, precio, stock):
        self.__nombre=nombre
        self.__precio=precio
        self.__stock=stock
        #lanzamos la excepcion ValueError con la condicion sobre precio y stock
        if precio < 0 or stock < 0:
            raise ValueError("El precio y el stock deben ser positivos")

    '''Añade getters y setters para precio y stock, de modo que si se intenta asignar un
    valor negativo, también lance una excepción'''

    # Getter y setter de precio
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser positivo")
        self.__precio = nuevo_precio

    # Getter y setter de stock
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El stock debe ser positivo")
        self.__stock = nuevo_stock

    # Getter y setter de nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


if __name__ == "__main__":


    #Creo dos listas. Una sera el inventario y otra los productos que se van a crear(la de productos admite valores negativos para probar la excepcion,mientras que la de inventario solo admitira valores correctos)
    inventario=[]
        
    productos=[
               
        ("Producto1", 10.50, 10),
        ("Producto2", 20.30, 20),
        ("Producto3", 30, 30),
        ("Producto4", -5, 15),
        ("Producto5", 15, -10)
    ]
    
    '''Maneja las excepciones que puedan producirse al crear los productos o al
        acceder a los atributos.'''   
     
    #Intentamos añadir los productos a la lista inventario manejando las excepciones
    for nombre, precio, stock in productos:
        try:
            producto = Producto(nombre, precio, stock)
            inventario.append(producto)
        except ValueError as e:
            print()
            print(f"Error al añadir el producto {nombre}: {e}. No se admiten valores negativos." )
    print("\n")


    '''Escribe una función que recorra la lista y muestre el nombre y el valor total de
    cada producto (precio * stock).'''

    def mostrar_inventario(inventario):
        for producto in inventario:
            try:
                valor_total = producto.precio * producto.stock
            except ValueError as e:
                print(f"Error al acceder a los atributos del producto {producto.nombre}: {e}")
            else:
                print(f"Nombre: {producto.nombre}, Valor total: {valor_total} €")   
  
                                
    print("Inventario de productos:")
    for producto in inventario:
        print(f"Nombre: {producto.nombre} - Precio: {producto.precio} € -  Stock: {producto.stock}")
    print("\n")
        






