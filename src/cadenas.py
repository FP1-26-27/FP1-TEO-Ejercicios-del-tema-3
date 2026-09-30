def invierte_cadena(texto: str) -> str:
    '''
    Invierte el texto que recibe por parámetro.

    Parámetros:
    - texto (str): El texto a invertir

    Devuelve:
    (str) El texto recibido, al revés.
    '''
    res = ""
    for c in texto:
        res = c + res
    return res

def es_palindromo(texto: str, ignora_espacios: bool = False, ignora_mayusculas: bool = False) -> bool:
    '''
    Devuelve True si el texto recibido es un palíndromo

    Parámetros:
    texto (str): el texto que queremos testear si es palíndromo
    ignora_espacios (bool): si es True, se ignorarán los espacios
    ignora_mayúsculas (bool): si es True, se ignorarán las mayúsculas/minúsculas
    '''
    if ignora_espacios:
        texto = texto.replace(" ", "")

    if ignora_mayusculas:
        texto = texto.lower()

    return texto == invierte_cadena(texto)

def estiliza_mensaje(texto: str, alterna_may_min: bool = True, sustituye_espacios: str = " ") -> str:
    '''
    Recibe una cadena y permite obtener otra con algunos cambios estéticos.

    Parámetros:
    alterna_may_min (bool): si es True, en el texto devuelto se intercalan letras mayúsculas
      y minúsculas. Los caracteres que no son letras se dejan tal como están, y no cuentan 
      para ir alternando entre mayúsculas y minúscula.
    sustituye_espacios (str): se utiliza la cadena indicada para sustituir cada uno de los
      espacios de la cadena de entrada por dicha cadena.

    Devuelve:
    (str) la cadena resultante
    '''
    res = ""
    toca_mayusculas = True
    for c in texto:
        if alterna_may_min and c.isalpha():
            if toca_mayusculas:
                c = c.upper()
            else:
                c = c.lower()
            toca_mayusculas = not toca_mayusculas

        # TODO: Implementar sustituye_espacios en casa

        res += c
    