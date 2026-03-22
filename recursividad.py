import sys


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        func = input("Funcion a evaluar: ")
        n = input("Valor a evaluar: ")
    if len(sys.argv) == 3:
        func = sys.argv[1]
        n = sys.argv[2]
    else:
        sys.exit("Error: Cantidad de parametros incorrecta")

    match func:
        case "factorial":
            print(factorial(int(n)))
        case "fibonacci":
            print(fibonacci(int(n)))