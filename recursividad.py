# Alumno: Cabrera Emanuel
import sys

# Algoritmos
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Ejercicio 1
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

# Ejercicio 2
def sumatoria(n):
    if n == 1:
        return 1
    else:
        return n + sumatoria(n-1)

# Ejercicio 3
def producto(n, m):
    if m == 0:
        return 0
    else:
        return n + producto(n, m - 1)

# Ejercicio 4
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)
    
# Ejercicio 5
def romanos(s):
    s = s.upper() # Me aseguro que el valor este en mayusculas
    valores = {
        'I':1, 'V':5, 'X':10, 'L':50,
        'C':100, 'D':500, 'M':1000
    } # Dict con los valroes correspondientes de los nros romanos
    # Condicion de corte:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return valores[s]
    
    # Si el primer caracter es menor al siguiente, restamos:
    if valores[s[0]] < valores[s[1]]:
        return valores[s[1]] - valores[s[0]] + romanos(s[2:])
    #... y luego le sumamos recursivamente el resto del string.
    # Si el primer caracter es mayor al siguiente, sumamos:
    else:
        return valores[s[0]] + romanos(s[1:])
    #... sumamos el valor actual al resto del string.

# Ejercicio 6
def invertido(s):
    if len(s) == 1:
        return s
    return s[-1] + invertido(s[:len(s)-1])

# Ejecicio 7:
def serie(n):
    if n == 1:
        return 1
    else:
        return 1/n + serie(n-1)
    
# Ejercicio 8:
def binario(n):
    if n == 0 | 1:
        return str(n)
    return binario(n//2) + str(n%2)

# Ejercicio 9:
def logaritmo(n, b):
    if n < b:
        return 0
    return logaritmo(n // b, b) + 1

# Ejecucion
if __name__ == "__main__":
    if len(sys.argv) == 3:
        func = sys.argv[1]
        a = sys.argv[2]
    elif len(sys.argv) == 4:
        func = sys.argv[1]
        a = sys.argv[2]
        b = sys.argv[3]
    else:
        sys.exit("Error: Cantidad de parametros incorrecta")

    match func:
        case "factorial":
            print(factorial(int(a)))
        case "fibonacci":
            print(fibonacci(int(a)))
        case "sumatoria":
            print(sumatoria(int(a)))
        case "producto":
            print(producto(int(a), int(b)))
        case "potencia":
            print(potencia(int(a), int(b)))
        case "romanos":
            print(romanos(a))
        case "invertido":
            print(invertido(a))
        case "serie":
            print(serie(int(a)))
        case "binario":
            print(binario(int(a)))
        case "logaritmo":
            print(logaritmo(int(a), int(b)))
