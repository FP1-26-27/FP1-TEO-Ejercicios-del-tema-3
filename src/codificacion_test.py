from codificacion import cifra_cesar, rompe_cesar

def test_cifra_cesar():
    print("Probando la función cifra_cesar...")
    assert cifra_cesar("Hola Mundo", 1) == "Ipmb Nvñep"
    assert cifra_cesar("Hola Mundo", 13) == "Téxn YBzpé"
    assert cifra_cesar("Hola Mundo", 66) == "Hola Mundo"

test_cifra_cesar()
print("Todos los tests son correctos.")

texto_codificado = "j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!"
print("Desencriptando el mensaje:", texto_codificado)
rompe_cesar(texto_codificado)