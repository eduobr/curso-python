def buscarHastaPrimeraVocal(palabra):
    contador = 0
    vocales="aeiou"
    while not(palabra[contador].lower() in vocales):
        contador=contador+1
    print(palabra[0:contador])


def buscarPrimeraVocalNuevo(palabra):
    i=0
    while i<len(palabra) and not(palabra[i].lower() in "aeiou"):
        print(palabra[i])
        i=i+1
        

