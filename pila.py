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
# class Baraja:
#     def __init__(self):
#         self._naipes = []
        
#     def __str__(self):
#         return f"Una baraja con {self.size()} naipes."
        
#     def apilar(self, naipe):
# 	    if naipe not in self._naipes:
#         	self._items.append(naipe)
#         if naipe._palo == "comodin" and self._naipes.count(naipe) < 2:
#             self._items.append(naipe)
        
#     def size(self):
#         return len(self._naipes)
        
#     def is_empty(self):
#         return (self.size() == 0)
        
#     def desapilar(self):
#         if not self.is_empty():
#             return self._items.pop()
#         else:
#             raise IndexError("Baraja vacia.")
    
#     def peek(self):
#         value = self.unstack()
#         self.stack(value)
#         return value

# class Naipe:
#     PALOS = ("basto", "espada", "oro", "copa")
#     def __init__(self):
#         if random() < 0.04:  # 4% de probabilidad
#             self._palo = "comodin"
#             self._valor = None
#         else:
#             self._palo = choice(Naipe.PALOS)
#             self._valor = randint(1, 12)
        
#     def __str__(self):
#         if self._palo == "comodin":
#             return "Comodin!!"
#         return f"{self._valor} de {self._palo}"
		
#     def __eq__(self, other):
#         return ((self._palo == other._palo) and (self._valor == other._valor))
		
# naipe1 = Naipe()
# naipe2 = Naipe()
# naipe3 = Naipe()
# naipe4 = Naipe()
# print(naipe1)

# Ejecucion
if __name__ == "__main__":
    # Generacion de instancias
    pila1 = Pila()
    
    # Carga de valores
    for i in range(10):
        pila1.apilar(randint(1,10))
    
    # Funcion/es a probar
    pila1.mostrar()
    pila1.invertir()
    pila1.mostrar()