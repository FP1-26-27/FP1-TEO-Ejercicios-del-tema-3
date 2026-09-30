from cadenas import *

def test_invierte_cadena():
    print("Probando invierte_cadena...")
    assert invierte_cadena("") == ""
    assert invierte_cadena("Texto de prueba") == "abeurp ed otxeT"
    assert invierte_cadena("seres") == "seres"

def test_es_palindromo():
    # TODO: Resolver en casa
    pass

def test_estiliza_mensaje():
    print("Probando estiliza_mensaje...")
    assert estiliza_mensaje("Fundamentos de programación 1") == "FuNdAmEnToS dE pRoGrAmAcIóN 1"
    # No vamos a implementar el parámetro usa_dieresis
    # assert estiliza_mensaje("Murciélago", usa_dieresis=True) == "MüRcÏéLäGö"
    assert estiliza_mensaje("Soy un programador experto", sustituye_espacios="*") == "SoY*uN*pRoGrAmAdOr*ExPeRtO"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=True, usa_dieresis=False, sustituye_espacios="_") == "HoLa_MuNdO"

test_invierte_cadena()
# TODO: Comprueba que se pasan bien los tests de estiliza_mensaje
# Para ello descomenta la siguiente línea
#test_estiliza_mensaje()
print("Todas las pruebas pasaron correctamente.")