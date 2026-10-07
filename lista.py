"""
Cómo ejecutarlo: Se hace uso de command line arguments
    python ejercicios.py        -> muestra un menú para elegir el ejercicio
    python ejercicios.py 1      -> ejecuta solo el ejercicio de Superhéroes
    python ejercicios.py 2      -> ejecuta solo el ejercicio de Pokémon
    python ejercicios.py 3      -> ejecuta ambos
"""
import sys
from typing import Any, Optional

class List(list):

    __CRITERION_FUNCTION = {}

    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function

    def show(self) -> None:
        for element in self:
            print(element)

    def search(self, search_value: Any, criterion: str = None) -> Optional[int]:
        self.sort_by_criterion(key_criterion=criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        start = 0
        end = len(self) - 1
        middle = (start + end) // 2

        while start <= end:

            if search_criterion is None and not isinstance(self[0], (bool, int, float, str)):
                print('no se pudo determinar criterio de busqueda')
                return None

            value = search_criterion(self[middle]) if search_criterion else self[middle]

            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1

            middle = (start + end) // 2

    def delete_value(self, value, criterion=None) -> Optional[Any]:
        index = self.search(value, criterion)

        return self.pop(index) if index is not None else None

    def sort_by_criterion(self, key_criterion=None) -> None:

        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)

        if sort_criterion:
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (bool, int, float, str)):
            self.sort()
        else:
            print('no se puede ordenar la lista no se como se debe ordenar')

    def size(self) -> int:
        return len(self)


def titulo(texto):
    print(f"\n--- {texto} ---")


#Ejercicio 1 Superheroes
H_NOMBRE = 'hero_name'
H_ANIO = 'hero_year'
H_CASA = 'hero_house'


class Superheroe:

    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (f"{self.nombre} | Año: {self.anio_aparicion} | "
                f"Casa: {self.casa} | Bio: {self.biografia}")


def heroe_por_nombre(item):
    return item.nombre


def heroe_por_anio(item):
    return item.anio_aparicion


def heroe_por_casa(item):
    return item.casa


def crear_lista_superheroes():
    lista = List()
    lista.add_criterion(H_NOMBRE, heroe_por_nombre)
    lista.add_criterion(H_ANIO, heroe_por_anio)
    lista.add_criterion(H_CASA, heroe_por_casa)

    datos = [
        ("Superman", 1938, "DC", "Último hijo de Krypton, criado en la Tierra por los Kent."),
        ("Batman", 1939, "DC", "Bruce Wayne combate el crimen en Gotham usando un traje con forma de murciélago."),
        ("Linterna Verde", 1940, "DC", "Posee un anillo de poder que crea construcciones de luz verde."),
        ("Flash", 1940, "DC", "Velocista que obtuvo sus poderes tras un accidente en su laboratorio."),
        ("Mujer Maravilla", 1941, "DC", "Princesa amazona de Temiscira, embajadora de paz."),
        ("Capitán América", 1941, "Marvel", "Soldado mejorado con el suero del supersoldado durante la Segunda Guerra."),
        ("Spider-Man", 1962, "Marvel", "Peter Parker fue picado por una araña radiactiva y usa un traje rojo y azul."),
        ("Hulk", 1962, "Marvel", "El científico Bruce Banner se transforma en un gigante verde por la ira."),
        ("Thor", 1962, "Marvel", "Dios nórdico del trueno que empuña el martillo Mjolnir."),
        ("Iron Man", 1963, "Marvel", "Tony Stark construyó una armadura tecnológica para proteger al mundo."),
        ("Dr. Strange", 1963, "DC", "Ex cirujano que se convirtió en el Hechicero Supremo."),
        ("Black Widow", 1964, "Marvel", "Espía rusa entrenada, devenida en agente de S.H.I.E.L.D."),
        ("Black Panther", 1966, "Marvel", "Rey de Wakanda, protegido por un traje de vibranium."),
        ("Capitana Marvel", 1968, "Marvel", "Piloto de la Fuerza Aérea que adquirió poderes cósmicos."),
        ("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor de curación."),
        ("Star-Lord", 1976, "Marvel", "Mestizo terrestre-ceresiano, líder de los Guardianes de la Galaxia."),
    ]
    for nombre, anio, casa, bio in datos:
        lista.append(Superheroe(nombre, anio, casa, bio))
    return lista


# a. eliminar el nodo que contiene la información de Linterna Verde
def eliminar_superheroe(lista, nombre):
    eliminado = lista.delete_value(nombre, H_NOMBRE)
    if eliminado:
        print(f"Se eliminó: {eliminado.nombre}")
    else:
        print(f"No se encontró a {nombre}")


# b. mostrar el año de aparición de Wolverine
def mostrar_anio_aparicion(lista, nombre):
    indice = lista.search(nombre, H_NOMBRE)
    if indice is not None:
        print(f"{nombre} apareció en {lista[indice].anio_aparicion}")
    else:
        print(f"No se encontró a {nombre}")


# c. cambiar la casa de Dr. Strange a Marvel
def cambiar_casa(lista, nombre, nueva_casa):
    indice = lista.search(nombre, H_NOMBRE)
    if indice is not None:
        lista[indice].casa = nueva_casa
        print(f"La casa de {nombre} ahora es {nueva_casa}")
    else:
        print(f"No se encontró a {nombre}")


# d. mostrar el nombre de los superhéroes cuya biografía menciona "traje" o "armadura"
def mostrar_por_palabras_en_bio(lista, palabras):
    for heroe in lista:
        bio = heroe.biografia.lower()
        if any(palabra in bio for palabra in palabras):
            print(heroe.nombre)


# e. mostrar nombre y casa de los superhéroes con fecha de aparición anterior a 1963
def mostrar_anteriores_a(lista, anio):
    for heroe in lista:
        if heroe.anio_aparicion < anio:
            print(f"{heroe.nombre} - {heroe.casa}")


# f. mostrar la casa a la que pertenecen ciertos superhéroes
def mostrar_casa(lista, nombres):
    for nombre in nombres:
        indice = lista.search(nombre, H_NOMBRE)
        if indice is not None:
            print(f"{nombre} pertenece a {lista[indice].casa}")
        else:
            print(f"No se encontró a {nombre}")


# g. mostrar toda la información de ciertos superhéroes
def mostrar_informacion(lista, nombres):
    for nombre in nombres:
        indice = lista.search(nombre, H_NOMBRE)
        if indice is not None:
            print(lista[indice])
        else:
            print(f"No se encontró a {nombre}")


# h. listar los superhéroes que comienzan con determinadas letras
def listar_por_iniciales(lista, letras):
    lista.sort_by_criterion(H_NOMBRE)  # para que el listado salga alfabético
    for heroe in lista:
        if heroe.nombre[0].upper() in letras:
            print(heroe.nombre)


# i. determinar cuántos superhéroes hay de cada casa
def contar_por_casa(lista):
    conteo = {}
    for heroe in lista:
        conteo[heroe.casa] = conteo.get(heroe.casa, 0) + 1
    for casa, cantidad in conteo.items():
        print(f"{casa}: {cantidad}")


def ejecutar_superheroes():
    print("=" * 60)
    print("  EJERCICIO 1: SUPERHÉROES")
    print("=" * 60)

    superheroes = crear_lista_superheroes()

    titulo("a. Eliminar a Linterna Verde")
    eliminar_superheroe(superheroes, "Linterna Verde")

    titulo("b. Año de aparición de Wolverine")
    mostrar_anio_aparicion(superheroes, "Wolverine")

    titulo("c. Cambiar la casa de Dr. Strange a Marvel")
    cambiar_casa(superheroes, "Dr. Strange", "Marvel")

    titulo('d. Biografía con "traje" o "armadura"')
    mostrar_por_palabras_en_bio(superheroes, ("traje", "armadura"))

    titulo("e. Aparición anterior a 1963")
    mostrar_anteriores_a(superheroes, 1963)

    titulo("f. Casa de Capitana Marvel y Mujer Maravilla")
    mostrar_casa(superheroes, ("Capitana Marvel", "Mujer Maravilla"))

    titulo("g. Información de Flash y Star-Lord")
    mostrar_informacion(superheroes, ("Flash", "Star-Lord"))

    titulo("h. Superhéroes que comienzan con B, M o S")
    listar_por_iniciales(superheroes, ("B", "M", "S"))

    titulo("i. Cantidad de superhéroes por casa")
    contar_por_casa(superheroes)


# Ejercicio 2 Entrenadores Pokemon
T_NOMBRE = 'trainer_name'
T_TORNEOS = 'trainer_tournaments'
P_NOMBRE = 'pokemon_name'
P_NIVEL = 'pokemon_level'


class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        subtipo = self.subtipo if self.subtipo else "-"
        return (f"{self.nombre} | Nivel: {self.nivel} | "
                f"Tipo: {self.tipo} | Subtipo: {subtipo}")


def pokemon_por_nombre(item):
    return item.nombre


def pokemon_por_nivel(item):
    return item.nivel


class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas,
                 batallas_ganadas, pokemons=None):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

        # Lista interna: cada entrenador tiene su propia List de Pokémons
        self.pokemons = List()
        self.pokemons.add_criterion(P_NOMBRE, pokemon_por_nombre)
        self.pokemons.add_criterion(P_NIVEL, pokemon_por_nivel)
        for pokemon in (pokemons or []):
            self.pokemons.append(pokemon)

    @property
    def porcentaje_ganadas(self):
        total = self.batallas_ganadas + self.batallas_perdidas
        return self.batallas_ganadas * 100 / total if total else 0.0

    def __str__(self):
        return (f"{self.nombre} | Torneos ganados: {self.torneos_ganados} | "
                f"Batallas ganadas: {self.batallas_ganadas} | "
                f"Batallas perdidas: {self.batallas_perdidas}")


def entrenador_por_nombre(item):
    return item.nombre


def entrenador_por_torneos(item):
    return item.torneos_ganados


def crear_lista_entrenadores():
    lista = List()
    lista.add_criterion(T_NOMBRE, entrenador_por_nombre)
    lista.add_criterion(T_TORNEOS, entrenador_por_torneos)

    lista.append(Entrenador("Ash", 7, 18, 82, [
        Pokemon("Pikachu", 58, "Eléctrico"),
        Pokemon("Charizard", 62, "Fuego", "Volador"),
        Pokemon("Sceptile", 55, "Planta"),
        Pokemon("Pelipper", 50, "Agua", "Volador"),
        Pokemon("Greninja", 60, "Agua", "Siniestro"),
    ]))
    lista.append(Entrenador("Misty", 3, 30, 70, [
        Pokemon("Staryu", 25, "Agua"),
        Pokemon("Starmie", 40, "Agua", "Psíquico"),
        Pokemon("Wingull", 22, "Agua", "Volador"),
        Pokemon("Staryu", 20, "Agua"),  
    ]))
    lista.append(Entrenador("Brock", 4, 25, 75, [
        Pokemon("Onix", 38, "Roca", "Tierra"),
        Pokemon("Geodude", 20, "Roca", "Tierra"),
        Pokemon("Vulpix", 33, "Fuego"),
        Pokemon("Tangela", 30, "Planta"),
        Pokemon("Tyrantrum", 45, "Roca", "Dragón"),
    ]))
    lista.append(Entrenador("Gary", 5, 12, 60, [
        Pokemon("Blastoise", 60, "Agua"),
        Pokemon("Arcanine", 56, "Fuego"),
        Pokemon("Umbreon", 50, "Siniestro"),
        Pokemon("Terrakion", 58, "Roca", "Lucha"),
    ]))
    lista.append(Entrenador("Cynthia", 2, 5, 95, [
        Pokemon("Garchomp", 66, "Dragón", "Tierra"),
        Pokemon("Lucario", 63, "Lucha", "Acero"),
        Pokemon("Togekiss", 62, "Hada", "Volador"),
        Pokemon("Milotic", 61, "Agua"),
        Pokemon("Spiritomb", 60, "Fantasma", "Siniestro"),
    ]))
    lista.append(Entrenador("Lance", 3, 15, 45, [
        Pokemon("Dragonite", 60, "Dragón", "Volador"),
        Pokemon("Gyarados", 58, "Agua", "Volador"),
        Pokemon("Charizard", 60, "Fuego", "Volador"),
        Pokemon("Dragonite", 55, "Dragón", "Volador"),  # repetido a propósito (ítem i)
    ]))
    return lista


def buscar_entrenador(lista, nombre):
    """Devuelve el entrenador con ese nombre, o None si no existe."""
    indice = lista.search(nombre, T_NOMBRE)
    return lista[indice] if indice is not None else None


# a. obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(lista, nombre_entrenador):
    entrenador = buscar_entrenador(lista, nombre_entrenador)
    if entrenador is None:
        print(f"No se encontró al entrenador {nombre_entrenador}")
        return None
    cantidad = entrenador.pokemons.size()
    print(f"{entrenador.nombre} tiene {cantidad} Pokémons")
    return cantidad


# b. listar los entrenadores que hayan ganado más de tres torneos
def listar_mas_de_tres_torneos(lista):
    for entrenador in lista:
        if entrenador.torneos_ganados > 3:
            print(f"{entrenador.nombre} - {entrenador.torneos_ganados} torneos")


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_del_mejor_entrenador(lista):
    if not lista:
        print("No hay entrenadores cargados")
        return
    lista.sort_by_criterion(T_TORNEOS)
    mejor = lista[-1]  # ordenado de menor a mayor: el último es el que más ganó
    if mejor.pokemons.size() == 0:
        print(f"{mejor.nombre} no tiene Pokémons")
        return
    mejor.pokemons.sort_by_criterion(P_NIVEL)
    pokemon = mejor.pokemons[-1]
    print(f"Entrenador con más torneos: {mejor.nombre} ({mejor.torneos_ganados})")
    print(f"Su Pokémon de mayor nivel: {pokemon}")


# d. mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_entrenador_completo(lista, nombre_entrenador):
    entrenador = buscar_entrenador(lista, nombre_entrenador)
    if entrenador is None:
        print(f"No se encontró al entrenador {nombre_entrenador}")
        return
    print(entrenador)
    print("Pokémons:")
    for pokemon in entrenador.pokemons:
        print(f"   - {pokemon}")


# e. mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %
def mostrar_por_porcentaje_ganadas(lista, minimo):
    for entrenador in lista:
        if entrenador.porcentaje_ganadas > minimo:
            print(f"{entrenador.nombre} - {entrenador.porcentaje_ganadas:.1f}% de batallas ganadas")


# f. entrenadores con Pokémons de tipo fuego y planta, o agua/volador (tipo y subtipo)
# Interpretación: (tiene algún Pokémon de tipo Fuego Y algún Pokémon de tipo Planta)
#                 O (tiene algún Pokémon con tipo Agua y subtipo Volador)
def tiene_tipo(entrenador, tipo):
    return any(p.tipo == tipo or p.subtipo == tipo for p in entrenador.pokemons)


def tiene_tipo_y_subtipo(entrenador, tipo, subtipo):
    return any(p.tipo == tipo and p.subtipo == subtipo for p in entrenador.pokemons)


def mostrar_por_tipos(lista):
    for entrenador in lista:
        fuego_y_planta = tiene_tipo(entrenador, "Fuego") and tiene_tipo(entrenador, "Planta")
        agua_volador = tiene_tipo_y_subtipo(entrenador, "Agua", "Volador")
        if fuego_y_planta or agua_volador:
            motivos = []
            if fuego_y_planta:
                motivos.append("Fuego + Planta")
            if agua_volador:
                motivos.append("Agua/Volador")
            print(f"{entrenador.nombre} ({' y '.join(motivos)})")


# g. el promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel(lista, nombre_entrenador):
    entrenador = buscar_entrenador(lista, nombre_entrenador)
    if entrenador is None:
        print(f"No se encontró al entrenador {nombre_entrenador}")
        return None
    if entrenador.pokemons.size() == 0:
        print(f"{entrenador.nombre} no tiene Pokémons")
        return None
    promedio = sum(p.nivel for p in entrenador.pokemons) / entrenador.pokemons.size()
    print(f"Promedio de nivel de {entrenador.nombre}: {promedio:.2f}")
    return promedio


# h. determinar cuántos entrenadores tienen a un determinado Pokémon
def contar_entrenadores_con_pokemon(lista, nombre_pokemon):
    cantidad = 0
    for entrenador in lista:
        if entrenador.pokemons.search(nombre_pokemon, P_NOMBRE) is not None:
            cantidad += 1
    print(f"{cantidad} entrenador(es) tienen a {nombre_pokemon}")
    return cantidad


# i. mostrar los entrenadores que tienen Pokémons repetidos
def mostrar_con_pokemons_repetidos(lista):
    for entrenador in lista:
        conteo = {}
        for pokemon in entrenador.pokemons:
            conteo[pokemon.nombre] = conteo.get(pokemon.nombre, 0) + 1
        repetidos = [f"{nombre} (x{veces})" for nombre, veces in conteo.items() if veces > 1]
        if repetidos:
            print(f"{entrenador.nombre}: {', '.join(repetidos)}")


# j. entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def mostrar_con_alguno_de(lista, nombres_pokemon):
    for entrenador in lista:
        encontrados = [n for n in nombres_pokemon
                       if entrenador.pokemons.search(n, P_NOMBRE) is not None]
        if encontrados:
            print(f"{entrenador.nombre}: {', '.join(encontrados)}")


# k. determinar si un entrenador "X" tiene al Pokémon "Y" (ambos nombres ingresados);
#    si lo tiene, mostrar los datos de ambos
def verificar_pokemon_de_entrenador(lista, nombre_entrenador, nombre_pokemon):
    entrenador = buscar_entrenador(lista, nombre_entrenador)
    if entrenador is None:
        print(f"No se encontró al entrenador {nombre_entrenador}")
        return
    indice = entrenador.pokemons.search(nombre_pokemon, P_NOMBRE)
    if indice is None:
        print(f"{entrenador.nombre} NO tiene a {nombre_pokemon}")
    else:
        print(f"{entrenador.nombre} SÍ tiene a {nombre_pokemon}")
        print(f"   Entrenador: {entrenador}")
        print(f"   Pokémon:    {entrenador.pokemons[indice]}")


def ejecutar_pokemon():
    print("=" * 60)
    print("  EJERCICIO 2: ENTRENADORES POKÉMON")
    print("=" * 60)

    entrenadores = crear_lista_entrenadores()

    titulo("a. Cantidad de Pokémons de Misty")
    cantidad_pokemons(entrenadores, "Misty")

    titulo("b. Entrenadores con más de 3 torneos ganados")
    listar_mas_de_tres_torneos(entrenadores)

    titulo("c. Pokémon de mayor nivel del entrenador con más torneos")
    pokemon_mayor_nivel_del_mejor_entrenador(entrenadores)

    titulo("d. Todos los datos de Brock y sus Pokémons")
    mostrar_entrenador_completo(entrenadores, "Brock")

    titulo("e. Entrenadores con más de 79% de batallas ganadas")
    mostrar_por_porcentaje_ganadas(entrenadores, 79)

    titulo("f. Pokémons de tipo Fuego y Planta, o Agua/Volador")
    mostrar_por_tipos(entrenadores)

    titulo("g. Promedio de nivel de los Pokémons de Ash")
    promedio_nivel(entrenadores, "Ash")

    titulo("h. Cuántos entrenadores tienen a Charizard")
    contar_entrenadores_con_pokemon(entrenadores, "Charizard")

    titulo("i. Entrenadores con Pokémons repetidos")
    mostrar_con_pokemons_repetidos(entrenadores)

    titulo("j. Entrenadores con Tyrantrum, Terrakion o Wingull")
    mostrar_con_alguno_de(entrenadores, ("Tyrantrum", "Terrakion", "Wingull"))

    titulo("k. ¿El entrenador X tiene al Pokémon Y?")
    verificar_pokemon_de_entrenador(entrenadores, "Gary", "Terrakion")   # lo tiene
    verificar_pokemon_de_entrenador(entrenadores, "Misty", "Pikachu")    # no lo tiene
    verificar_pokemon_de_entrenador(entrenadores, "Red", "Pikachu")      # no existe el entrenador


# ======================================================================
#  4. MENÚ PRINCIPAL
# ======================================================================
def ejecutar_opcion(opcion):
    if opcion == "1":
        ejecutar_superheroes()
    elif opcion == "2":
        ejecutar_pokemon()
    elif opcion == "3":
        ejecutar_superheroes()
        print()
        ejecutar_pokemon()
    else:
        print("Opción inválida")


def main():
    # Si se pasa el número por la línea de comandos, se ejecuta directo
    if len(sys.argv) > 1:
        ejecutar_opcion(sys.argv[1])
        return

    while True:
        print("\n===== MENÚ =====")
        print("1. Ejercicio Superhéroes")
        print("2. Ejercicio Pokémon")
        print("3. Ejecutar ambos")
        print("0. Salir")
        try:
            opcion = input("Elegí una opción: ").strip()
        except EOFError:
            break
        if opcion == "0":
            break
        ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()