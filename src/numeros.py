def invierte_numero(numero: int) -> int:
    '''
    Devuelve el número con los dígitos invertidos
    '''
    res = 0
    while numero != 0:
        ultima_cifra = numero % 10
        res = res * 10 + ultima_cifra
        numero //= 10 # significa: numero = numero // 10
    return res

def convierte_binario(numero: int) -> str:
    '''
    Convierte un número entero en binario
    '''

    if numero == 0:
        return "0"

    res = ""
    while numero != 0:
        numero, resto = numero // 2, numero % 2
        # Si queremos, podemos hacerlo en dos asignaciones, pero SIEMPRE
        # empezando por el resto:
        # resto = numero % 2
        # numero = numero // 2
        res = str(resto) + res # Concatena el digito que ha salido en "resto" por la izquierda
    return res 


def sumar_divisores_propios(numero: int) -> int:
    '''
    Devuelve la suma de los divisores propios del número recibido.
    '''
    res = 0
    for i in range(1, numero):
        if numero % i == 0: # i es divisor de numero
            res += i
    return res


def clasifica_numero(numero: int) -> str:
    '''
    Devuelve una cadena indicando si el número recibido es
    "PERFECTO", "ABUNDANTE" o "DEFICIENTE".
    '''
    suma_divisores = sumar_divisores_propios(numero)
    if suma_divisores == numero:
        return "PERFECTO"
    elif suma_divisores > numero:
        return "ABUNDANTE"
    else:
        return "DEFICIENTE"

def clasifica_rango(limite: int) -> None:
    '''
    Muestra la clasificación de todos los números
    desde 1 hasta límite
    '''
    for i in range(1, limite+1):
        print(f"{i}: {clasifica_numero(i)}")

def busca_perfecto(posicion: int) -> int:
    '''
    Busca y devuelve el número perfecto cuya posición se indique.
    Por ejemplo, si posicion es 1, se devuelve el primer número perfecto (6).
    '''
    n = 1
    contador = 0
    while True:
        if clasifica_numero(n) == "PERFECTO":
            contador += 1
            if contador == posicion:
                return n
        n += 1