ALFABETO = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def letra_a_posicion(letra: str) -> int:
    posicion = ALFABETO.find(letra)
    if posicion == -1:  
        return None
    else:
        return posicion

def posicion_a_letra(posicion):
    if 0 <= posicion < len(ALFABETO):
        return ALFABETO[posicion]
    else:
        return None

def cifra_cesar(texto: str, clave: int) -> str:
    res = ""
    for c in texto:
        posicion = letra_a_posicion(c)
        if posicion == None:
            res += c
        else:
            nueva_posicion = (posicion + clave) % len(ALFABETO)
            res += posicion_a_letra(nueva_posicion)
    return res

def rompe_cesar(texto_codificado: str) -> None:
    for clave in range(len(ALFABETO)):
        texto = cifra_cesar(texto_codificado, -clave)
        print(f"(clave {clave}): {texto}")

