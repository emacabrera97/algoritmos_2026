# La pila es una sucesion elementos "apilados", posee dos funcionalidades 
# basicas: apilar un nuevo elemento, desapilar un elemento. El ultimo
# en entrar es el primero en salir, como una pila de platos por ejemplo.

class Pila:
    def __init__(self):
        self.__elementos = []

    @property
    def elementos(self):
        return self.__elementos

    def apilar(self, value):
        self.__elementos.append(value)
    
    def desapilar(self):
        return self.__elementos.pop()

    def size(self):
        return len(self.elementos)