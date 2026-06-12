

"""
Cola (Queue): Estructura de datos lineal que funciona siguiendo el principio FIFO (First In, First Out), 
donde el primer elemento en ingresar es el primero en salir.
Las operaciones principales son enqueue (encolar), dequeue (desencolar) y peek (ver el primer elemento).
"""

from typing import Any
from datetime import time
from bpila import Stack

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty:
            raise IndexError("Cannot dequeue from empty queue.")
        return self._items.pop(0)
    
    @property
    def size(self):
        return len(self._items)
    
    @property
    def is_empty(self):
        return self.size == 0
    
    @property
    def front(self):
        if self.is_empty:
            raise IndexError("Empty queue has no front.")
        return self._items[0]

    def move_front_to_back(self):
        self.enqueue(self.dequeue())


# Ejercicio 10
class Notification:
    def __init__(self, socialMedia, pubTime, content = ""):
        self.socialMedia = socialMedia
        hour, minutes = pubTime.split(":")
        self.pubTime = time(int(hour), int(minutes))
        self.content = content
    
    def __str__(self):
        return f"{self.socialMedia}({self.pubTime}): {self.content}"


class NotificationsQueue(Queue):
    # Inciso a
    def remove_notifications_from(self, to_remove):
        n = self.size
        for _ in range(n):
            if self.front.socialMedia == to_remove:
                self.dequeue()
            else:
                self.move_front_to_back()
    # Inciso b
    def filter_tweets(self, pattern):
        n = self.size
        for _ in range(n):
            if (self.front.socialMedia == "twitter") and (pattern in self.front.content):
                print(self.front)
            self.move_front_to_back()
    # Inciso c
    def filter_by_time_range(self, time_a, time_b):
        aux_stack = Stack()
        hour_a, minutes_a = time_a.split(":")
        hour_b, minutes_b = time_b.split(":")
        start_time = time(int(hour_a), int(minutes_a))
        end_time= time(int(hour_b), int(minutes_b)) 
        n = self.size
        for _ in range(n):
            if start_time <= self.front.pubTime <= end_time:
                aux_stack.push(self.front)
            self.move_front_to_back()
        return aux_stack.size, aux_stack
        

 # Ejercicio 22
class Hero:
    def __init__(self, realName, heroName, gender):
        self.realName = realName
        self.heroName = heroName
        self.gender = gender
        
    def __str__(self):
        return f"{self.heroName}: {self.realName}, {self.gender}"


class HeroQueue(Queue):
    # Inciso a
    def look_for_real_name(self, hero):
        n = self.size
        result = None
        for _ in range(n):
            if self.front.heroName == hero:
                result = self.front.realName
            self.move_front_to_back()
        return result
    # Inciso d y f
    def look_for_hero_name(self, name):
        n = self.size
        result = None
        for _ in range(n):
            if self.front.realName == name:
                result = self.front.heroName
            self.move_front_to_back()
        return result
    # Inciso b y c
    def list_by_gender(self, g):
        n = self.size
        result = []
        for _ in range(n):
            if self.front.gender == g:
                print(self.front)
            self.move_front_to_back()
    # Inciso e:
    def list_by_first_letter(self, letter):
        n = self.size
        for _ in range(n):
            if self.front.heroName.upper().startswith(letter.upper()):
                print(self.front)
            self.move_front_to_back()

if __name__ == "__main__":
    # ──────────────────────────────────────────
    #  DATOS DE PRUEBA
    # ──────────────────────────────────────────
    nq = NotificationsQueue()
    nq.enqueue(Notification("twitter",   "08:00", "Hello world #python"))
    nq.enqueue(Notification("instagram", "09:15", "Foto de vacaciones"))
    nq.enqueue(Notification("twitter",   "10:30", "Nuevo tutorial #python"))
    nq.enqueue(Notification("facebook",  "11:00", "Evento familiar"))
    nq.enqueue(Notification("twitter",   "12:45", "Hilo sobre IA"))
    nq.enqueue(Notification("instagram", "13:00", "Reel de cocina"))

    hq = HeroQueue()
    hq.enqueue(Hero("Tony Stark",      "Iron Man",    "M"))
    hq.enqueue(Hero("Natasha Romanova", "Black Widow", "F"))
    hq.enqueue(Hero("Steve Rogers",    "Captain America", "M"))
    hq.enqueue(Hero("Carol Danvers",   "Captain Marvel",  "F"))
    hq.enqueue(Hero("Bruce Banner",    "Hulk",        "M"))
    hq.enqueue(Hero("Wanda Maximoff",  "Scarlet Witch","F"))

    # ──────────────────────────────────────────
    #  MENÚ PRINCIPAL
    # ──────────────────────────────────────────
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. NotificationsQueue (Ejercicio 10)")
        print("2. HeroQueue          (Ejercicio 22)")
        print("0. Salir")
        opcion = input("Selecciona: ").strip()

        # ── NOTIFICATIONS ──────────────────────
        if opcion == "1":
            while True:
                print("\n--- NotificationsQueue ---")
                print(f"  Notificaciones en cola: {nq.size}")
                print("  a) Eliminar por red social")
                print("  b) Filtrar tweets por patrón")
                print("  c) Filtrar por rango de tiempo")
                print("  v) Ver cola actual")
                print("  r) Reiniciar datos de prueba")
                print("  0) Volver")
                sub = input("  Selecciona: ").strip()

                if sub == "a":
                    red = input("  Red social a eliminar (twitter/instagram/facebook): ").strip()
                    nq.remove_notifications_from(red)
                    print(f"  Notificaciones de '{red}' eliminadas. Cola actual ({nq.size}):")
                    nq.filter_tweets("")     # Recorre sin filtrar
                    n = nq.size
                    for _ in range(n):
                        print(" ", nq.front)
                        nq.move_front_to_back()

                elif sub == "b":
                    patron = input("  Patrón a buscar en tweets: ").strip()
                    print(f"  Tweets con '{patron}':")
                    nq.filter_tweets(patron)

                elif sub == "c":
                    t1 = input("  Hora inicio (HH:MM): ").strip()
                    t2 = input("  Hora fin   (HH:MM): ").strip()
                    cantidad, pila = nq.filter_by_time_range(t1, t2)
                    print(f"  Notificaciones en rango: {cantidad}")
                    while not pila.is_empty:
                        print(" ", pila.pop())

                elif sub == "v":
                    print(f"  Cola actual ({nq.size} elementos):")
                    n = nq.size
                    for _ in range(n):
                        print(" ", nq.front)
                        nq.move_front_to_back()

                elif sub == "r":
                    nq = NotificationsQueue()
                    nq.enqueue(Notification("twitter",   "08:00", "Hello world #python"))
                    nq.enqueue(Notification("instagram", "09:15", "Foto de vacaciones"))
                    nq.enqueue(Notification("twitter",   "10:30", "Nuevo tutorial #python"))
                    nq.enqueue(Notification("facebook",  "11:00", "Evento familiar"))
                    nq.enqueue(Notification("twitter",   "12:45", "Hilo sobre IA"))
                    nq.enqueue(Notification("instagram", "13:00", "Reel de cocina"))
                    print("  Datos de prueba restaurados.")

                elif sub == "0":
                    break
                else:
                    print("  Opción no válida.")

        # ── HEROES ────────────────────────────
        elif opcion == "2":
            while True:
                print("\n--- HeroQueue ---")
                print(f"  Héroes en cola: {hq.size}")
                print("  a) Buscar nombre real por nombre de héroe")
                print("  b) Listar por género  (M / F)")
                print("  c) Buscar nombre de héroe por nombre real")
                print("  d) Listar por primera letra del nombre de héroe")
                print("  v) Ver cola actual")
                print("  r) Reiniciar datos de prueba")
                print("  0) Volver")
                sub = input("  Selecciona: ").strip()

                if sub == "a":
                    heroe = input("  Nombre de héroe: ").strip()
                    res = hq.look_for_real_name(heroe)
                    print(f"  Nombre real: {res}" if res else "  Héroe no encontrado.")

                elif sub == "b":
                    genero = input("  Género (M/F): ").strip().upper()
                    print(f"  Héroes de género '{genero}':")
                    hq.list_by_gender(genero)

                elif sub == "c":
                    nombre = input("  Nombre real: ").strip()
                    res = hq.look_for_hero_name(nombre)
                    print(f"  Nombre de héroe: {res}" if res else "  Persona no encontrada.")

                elif sub == "d":
                    letra = input("  Primera letra: ").strip()
                    print(f"  Héroes cuyo nombre empieza con '{letra.upper()}':")
                    hq.list_by_first_letter(letra)

                elif sub == "v":
                    print(f"  Cola actual ({hq.size} héroes):")
                    n = hq.size
                    for _ in range(n):
                        print(" ", hq.front)
                        hq.move_front_to_back()

                elif sub == "r":
                    hq = HeroQueue()
                    hq.enqueue(Hero("Tony Stark",       "Iron Man",        "M"))
                    hq.enqueue(Hero("Natasha Romanova",  "Black Widow",     "F"))
                    hq.enqueue(Hero("Steve Rogers",     "Captain America", "M"))
                    hq.enqueue(Hero("Carol Danvers",    "Captain Marvel",  "F"))
                    hq.enqueue(Hero("Bruce Banner",     "Hulk",            "M"))
                    hq.enqueue(Hero("Wanda Maximoff",   "Scarlet Witch",   "F"))
                    print("  Datos de prueba restaurados.")

                elif sub == "0":
                    break
                else:
                    print("  Opción no válida.")

        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")