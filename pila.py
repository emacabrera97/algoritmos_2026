from random import choice, randint, random
# La pila es una sucesion elementos "apilados", posee dos funcionalidades 
# basicas: apilar un nuevo elemento, desapilar un elemento. El ultimo
# en entrar es el primero en salir, como una pila de platos por ejemplo.

class Pila:
    def __init__(self):
        self.__elementos = []

    def apilar(self, value):
        self.__elementos.append(value)
    
    def desapilar(self):
        return self.__elementos.pop()

    def size(self):
        return len(self.__elementos)
    
    def cima(self):
        return self.__elementos[-1]
    
    def mostrar(self):
        pila_aux = Pila()
        while self.size() > 0:
            value = self.desapilar()
            print(value, end = " ")
            pila_aux.apilar(value)
        print()
        while pila_aux.size() > 0:
            value = pila_aux.desapilar()
            self.apilar(value)
    
    #ejercicio1
    def ocurrencias(self, n: int):
        count = 0
        pila_aux = Pila()
        while self.size() > 0:
            value = self.desapilar()
            if value == n:
                count += 1
            pila_aux.apilar(value)
        while pila_aux.size() > 0:
            value = pila_aux.desapilar()
            self.apilar(value)
        return count

    #ejercicio2
    def solo_pares(self):
        pila_aux = Pila()
        while self.size() > 0:
            value = self.desapilar()
            if value % 2 == 0:
                pila_aux.apilar(value)
        while pila_aux.size() > 0:
            value = pila_aux.desapilar()
            self.apilar(value)
        
    # Ejercicio 3
    def reemplazar(self, a_reemplazar, reemplazo):
        stack_aux = Pila()
        while self.size() > 0:
            valor_actual = self.desapilar()
            if valor_actual == a_reemplazar:
                stack_aux.apilar(reemplazo)
            else:
                stack_aux.stack(valor_actual)
        while stack_aux.size() > 0:
            valor_actual = stack_aux.desapilar()
            self.stack(valor_actual)
    
    # Ejercicio 4
    def invertir(self):
        stack_aux = Pila()
        for i in range(self.size()):
            var_aux = self.desapilar()
            for _ in range(self.size() - i):
                valor = self.desapilar()
                stack_aux.apilar(valor)
            self.apilar(var_aux)
            while stack_aux.size() > 0:
                valor = stack_aux.desapilar()
                self.apilar(valor)

    #Ejercicio 7
    def eliminar(self, n:int):
        aux = Pila()
        for _ in range(n + 1):
            actual = self.desapilar()
            aux.apilar(actual)
        aux.desapilar()
        while aux.size() > 0:
            actual = aux.desapilar()
            self.apilar(actual)

# Ejercicio 5
def es_palindromo(cadena):
    cadena = cadena.lower()
    pila = Pila()
    [pila.apilar(letra) for letra in cadena]
    pila.invertir()
    inverso = "".join([pila.desapilar() for letra in cadena])
    return (inverso == cadena)

# Ejercicio 6
def dar_vuelta(cadena):
    cadena = cadena.lower()
    pila = Pila()
    [pila.apilar(letra) for letra in cadena]
    pila.invertir()
    return "".join([pila.desapilar() for letra in cadena])

# #Ejercicio8 (a terminar)
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

class Baraja:
    def __init__(self, nro_cartas: int = 48):
        self._naipes = []
        if not nro_cartas == 0: 
            while self.size() < nro_cartas:
                naipe = Naipe()
                self.apilar(naipe)

    def __str__(self):
        return f"Una baraja con {self.size()} naipes."
        
    def apilar(self, naipe):
        if naipe not in self._naipes:
            self._naipes.append(naipe)
        
    def size(self):
        return len(self._naipes)
        
    def esta_vacia(self):
        return (self.size() == 0)
        
    def desapilar(self):
        if not self.esta_vacia():
            return self._naipes.pop()
        else:
            raise IndexError("Baraja vacia.")
        
    def cima(self):
        return self._naipes[-1]
        
    def separar_por_palo(self):
        espadas, bastos, copas, oros = Baraja(nro_cartas=0), Baraja(nro_cartas=0), Baraja(nro_cartas=0), Baraja(nro_cartas=0)
        for i in range(self.size()):
            carta = self.desapilar()
            match carta.palo:
                case "espada":
                    espadas.apilar(carta)
                case "basto":
                    bastos.apilar(carta)
                case "oro":
                    oros.apilar(carta)
                case "copa":
                    copas.apilar(carta)
        return {
            "espada": espadas,
            "basto": bastos,
            "copa": copas,
            "oro": oros
        }
    
    def ordenar(self):
        pila_aux = Baraja(nro_cartas=0)
        while not self.esta_vacia():
            en_mano = self.desapilar()
            pila_aux.apilar(en_mano)
        while not pila_aux.esta_vacia():
            temp = pila_aux.desapilar()
            while not self.esta_vacia() and self.cima().valor < temp.valor:
                tmp = self.desapilar()
                pila_aux.apilar(tmp)
            self.apilar(temp)

# Ejecucion
if __name__ == "__main__":
    # Generacion de instancias
    baraja1 = Baraja()
    
    # Funcion/es a probar
    pilas = baraja1.separar_por_palo()
    for _ in range(pilas["espada"].size()):
        print(pilas["espada"].desapilar())
    