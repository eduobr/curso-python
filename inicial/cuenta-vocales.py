def cuentaVocales(palabra):
    '''(str)->int
        Devuelve el número de vocales que tiene s.
        '''
	palabraMin = palabra.lower()
	contador=0
	for caracter in palabraMin:
		if caracter in "aeiou":
			contador = contador+1
	return contador
