from random import choice, randint

"""
Pila (Stack): Estructura de datos lineal que funciona siguiendo el principio LIFO (Last In, First Out), 
donde el último elemento en ingresar es el primero en salir.
Las operaciones principales son push (apilar), pop (desapilar) y peek (ver el elemento superior).
"""

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def size(self):
        return len(self._items)
    
    def is_empty(self):
        return self.size() == 0
    
    def peek(self): # Tambien puede llamarse top
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def show(self):
        print(self._items)

    # Ejercicio 1
    def count(self, n: int):
        counter = 0
        aux = Stack()
        while self.size() > 0:
            value = self.pop()
            if value == n:
                counter += 1
            aux.push(value)
        while aux.size() > 0:
            value = aux.pop()
            self.push(value)
        return counter

    # Ejercicio 2
    def evens(self):
        aux = Stack()
        while self.size() > 0:
            value = self.pop()
            if value % 2 == 0:
                aux.push(value)
        while aux.size() > 0:
            value = aux.pop()
            self.push(value)
        
    # Ejercicio 3
    def replace(self, to_replace, new_value):
        aux = Stack()
        while self.size() > 0:
            current = self.pop()
            if current == to_replace:
                aux.push(new_value)
            else:
                aux.push(current)
        while aux.size() > 0:
            current = aux.pop()
            self.push(current)
    
    # Ejercicio 4
    def invert(self):
        aux = Stack()
        for i in range(self.size()):
            current = self.pop()
            for _ in range(self.size() - i):
                value = self.pop()
                aux.push(value)
            self.push(current)
            while aux.size() > 0:
                value = aux.pop()
                self.push(value)

    # Ejercicio 5
    @staticmethod
    def palindrome(s: str):
        s = s.lower()
        aux = Stack()
        [aux.push(l) for l in s]
        reversed = "".join([aux.pop() for l in s])
        return (reversed == s)

    # Ejercicio 6
    @staticmethod
    def invertString(s: str):
        s = s.lower()
        aux = Stack()
        [aux.push(l) for l in s]
        return "".join([aux.pop() for l in s])

    #Ejercicio 7
    def remove(self, n:int):
        aux = Stack()
        for _ in range(n + 1):
            current = self.pop()
            aux.push(current)
        aux.pop()
        while aux.size() > 0:
            current = aux.pop()
            self.push(current)


# Ejercicio 8
class Naipe:
    PALOS = ("basto", "espada", "oro", "copa")
    
    def __init__(self):
            self._palo = choice(Naipe.PALOS)
            self._valor = randint(1, 12)
        
    def __str__(self):
        return f"{self.valor} de {self.palo}"
        
    def __eq__(self, other: Naipe):
        return ((self.palo == other.palo) and (self.valor == other.valor))
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def valor(self):
        return self._valor

class Baraja(Stack):
    def __init__(self, nro_cartas: int = 48):
        super().__init__()
        self._presentes: set[tuple] = set()
        if not nro_cartas == 0: 
            while self.size() < nro_cartas:
                naipe = Naipe()
                self.apilar(naipe)

    def __str__(self):
        return f"Una baraja con {self.size()} naipes."
        
    def apilar(self, naipe: Naipe):
        clave = (naipe.palo, naipe.valor)
        if clave not in self._presentes:
            self._presentes.add(clave)
            self.push(naipe)
        
    def esta_vacia(self):
        return (self.size() == 0)
        
    def desapilar(self) -> Naipe:
        if self.esta_vacia():
            raise IndexError("Baraja vacía.")
        naipe = self.pop()
        self._presentes.discard((naipe.palo, naipe.valor))
        return naipe
        
    def separar_por_palo(self) -> dict["str", "Baraja"]:
        pilas = {palo: Baraja(nro_cartas=0) for palo in Naipe.PALOS}
        temp = []
        while not self.esta_vacia():
            carta = self.desapilar()
            temp.append(carta)
            pilas[carta.palo].apilar(carta)
        for carta in reversed(temp):  # restaura el orden original
            self.apilar(carta)
        return pilas
    
    def ordenar(self):
        aux = Baraja(nro_cartas=0)
        while not self.esta_vacia():
            aux.apilar(self.desapilar())
        while not aux.esta_vacia():
            temp = aux.desapilar()
            while not self.esta_vacia() and self.peek().valor < temp.valor:
                aux.apilar(self.desapilar())
            self.apilar(temp)


#Ejercicio 20    
def input_trayectoria(movimientos):
    while True:
        entrada = input("Ingrese un movimiento (direccion pasos): ")
        if not entrada:
            break
        direccion, distancia = entrada.split(" ")
        if direccion not in ("norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste", "suroeste"):
            print("ERROR: Dirección inválida")
            continue                         
        if not distancia.isnumeric():
            print("ERROR: La distancia debe ser un número entero")
            continue                         
        movimientos.push((direccion, distancia))  

def volver_al_comienzo(movimientos):
    opuestos = {
        "norte": "sur",
        "sur": "norte",
        "este": "oeste",
        "oeste": "este",
        "noreste": "suroeste",
        "suroeste": "noreste",
        "noroeste": "sureste",
        "sureste": "noroeste",
    }
    while movimientos.size() > 0:
        direccion, pasos = movimientos.pop()
        print((opuestos[direccion], pasos))


#Ejercicio 24
class Heroes(Stack):
    def look_for_character(self, *args):
        """
        El proposito de esta funcion es retornar la posicion
        de los heroes buscados.
        """
        results  = []
        aux = Stack()
        i = 1
        while self.size() > 0:
            current = self.pop()
            character, _ = current
            if character in args:
                results.append((character, i))
            aux.push(current)
            i += 1
        while aux.size() > 0:
            self.push(aux.pop())
        return results

    def more_than_5_movies(self):
        """
        Retornar aquellos personajes que aparezcan en mas de 5
        peliculas.
        """
        results = []
        for character, movies in self._items:
            if movies >= 5:
                results.append((character, movies))
        return results

    def whose_name_starts_with(self, letter):
        """
        Aquellos personajes cuyos nombres empiezan con...
        """
        results = []
        for character, _ in self._items:
            if character[0] == letter:
                results.append(character)
        return results

# Ejecucion
if __name__ == "__main__":
    opc = "1"
    #Testeo ejercicio 20
    while opc == "1":
        print("Testeando ejercicio 20")
        trayectoria = Stack()
        print("Ingrese los movimientos con el formato: direccion:str distancia:int")
        print("No ingrese nada para terminar la carga")
        input_trayectoria(trayectoria)
        print("=== Trayectoria cargada (fondo → cima) ===")
        trayectoria.show()
        print("\n=== Secuencia para volver al origen ===")
        volver_al_comienzo(trayectoria)
        opc = input("Ingrese 1 para volver a testear, cualquier otro valor para continuar...")
    print()
    print()
    print()
    #Testeo ejercicio 24
    opc = "1"
    while opc == "1":
        print("Testeando ejercicio 24")
        heroes = Heroes()
        mcu = [
        ("Iron Man", 10),
        ("Captain America", 7),
        ("Thor", 8),
        ("Black Widow", 7),
        ("Hulk", 6),
        ("Rocket Raccoon", 5),  
        ("Hawkeye", 5),
        ("Spider-Man", 6),
        ("Doctor Strange", 4),
        ("Black Panther", 3),
        ("Wanda", 5),
        ("Vision", 3),
        ("Ant-Man", 3),
        ("Star-Lord", 4),
        ("Groot", 4),           
        ("Gamora", 3),
        ("Nebula", 4),
        ("War Machine", 5),
        ("Falcon", 4),
        ("Bucky", 4),
        ("Nick Fury", 8),
        ("Wong", 4),
        ]
        for personaje in mcu:
            heroes.push(personaje)
        #Posicion de Rocket y Groot
        print("=== Buscando a Rocket y Groot ===")
        print(heroes.look_for_character("Rocket Raccoon", "Groot"))
        #Personajes que aparecen en mas de 5 peliculas
        print("\n=== Heroes en mas de 5 pelis ===")
        print(heroes.more_than_5_movies())
        #Personajes cuyos nombres empiezan con...
        print("\n=== Heroes cuyo nombre empieza con 'C' ===")
        print(heroes.whose_name_starts_with("C"))
        print("\n=== Heroes cuyo nombre empieza con 'D' ===")
        print(heroes.whose_name_starts_with("D"))
        print("\n=== Heroes cuyo nombre empieza con 'G' ===")
        print(heroes.whose_name_starts_with("G"))
        opc = input("Ingrese 1 para volver a testear, cualquier otro valor para terminar...")