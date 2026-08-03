from random import choice, randint

"""
Tabla hash: es tabla asociativa o tabla de dispersión es una colección estática de n
elementos a loes que podemos acceder de manera directa utilizando una función denominada hash
que transforma una clave (dato o parte de él) en una posición de memoria.
"""

legions = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

for i in range(10):
     trooper = f'{choice(legions)}-{randint(1000,9999)}'
     print(trooper)

