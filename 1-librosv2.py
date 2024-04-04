class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

lista_libros = []

libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Ficcion", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficcion", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasia", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clasico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clasico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasia", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Historica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasia", 4.0)

lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)
lista_libros.append(libro4)
lista_libros.append(libro5)
lista_libros.append(libro6)
lista_libros.append(libro7)
lista_libros.append(libro8)
lista_libros.append(libro9)
lista_libros.append(libro10)


def agregar_libro():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor del libro: ")
    genero = input("Ingrese el genero del libro: ")
    puntuacion_del_libro = float(input("Ingrese la puntuacion del libro: "))
    libro = Libro(titulo, autor, genero, puntuacion_del_libro)
    lista_libros.append(libro)
    print("El libro se agrego con exito en la lista")

def buscar_libro_por_genero():
    genero_buscado = input("Ingrese el genero de libro que esta buscando: ")
    generos_de_libros = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero_buscado.lower()]
    if generos_de_libros:
        print(f"Los libros del genero {genero_buscado} son los siguientes:")
        for titulo in generos_de_libros:
            print(titulo)
    else:
        print("No tenemos libros del genero {genero_buscado}")

def recomendacion_libro():
    genero_interes = input("Ingrese el genero que le gustaria leer: ")
    generos_de_libros = [libro for libro in lista_libros if libro.genero.lower() == genero_interes.lower()]
    if generos_de_libros:
        libro_recomendado = max(generos_de_libros, key=lambda x: x.puntuacion)
        print(f"El libro que te recomendamos es {libro_recomendado.titulo}")
    else:
        print("No tenemos ningun libro de ese genero para recomendarte")

while True:
    print("Buenos dias, se mostraran las acciones que se pueden realizar")
    print("*"*50)
    print("1. Agregar libro")
    print("2. Buscar libro por genero")
    print("3. Recomendar libro")
    print("4. Salir")
    
    opcion = input("Ingrese el numero de accion que desea realizar: ")
    
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        buscar_libro_por_genero()
    elif opcion == "3":
        recomendacion_libro()
    elif opcion == "4":
        print("Gracias por usar nuestro sistema de recomendacion de libros. Hasta luego")
        break
    else:
        print("Opcion no valida, por favor ingrese un numero del 1 al 4")