
def resumen(combinaciones):
	'''
		Muestra la cantidad de combinaciones por longitud y el total.
	'''
	
	print('Resumen')
	print('-' * 15)
	total = 0
	
	for x in range(len(combinaciones)):
		
		longitud = len(combinaciones[x])
		total += longitud
		print('Combinaciones de:', x, '=', longitud)
	
	print('-' * 30)
	print('Total:', total)


def puedeMoverse(ficha, fichas, lista):
	'''
		Verifica si la ficha actual puede moverse adelante.
	'''
	
	# Futura posicion de la ficha no se sale de la lista ni es posicion de otra ficha?
	return ((ficha + 1) != len(lista)) and ((ficha + 1) not in fichas)


def atraerFichas(ficha_pos, fichas):
	'''
		Mueve justo a la 'derecha' las fichas que estan a la derecha de la ficha actual.
	'''
	
	# La ultimo ficha no tiene nada a la derecha?
	if ficha_pos == (len(fichas) -1):
		
		return # Sale.
	
	der = fichas[ficha_pos + 1: ] # Fichas a la derecha de la ficha actual.
	
	for x in range(len(der)):
		
		# Hacer que las fichas a la derecha sean continuos a la ficha actual.
		fichas[ficha_pos + (x + 1)] = fichas[ficha_pos] + (x + 1)


def moverFicha(fichas, lista):
	'''
		Mueve hacia adelante la primer ficha que se puede mover, si hay.
		O sea, combinaciones de m elementos en n elementos.
	'''
	
	# Recorre las fichas de derecha a izquierda.
	for x in range(len(fichas) - 1, -1, -1):
		
		# La ficha en x se puede mover?
		if puedeMoverse(fichas[x], fichas, lista):
			
			fichas[x] += 1 # Mueve la ficha hacia delante.
			atraerFichas(x, fichas) # Atrae las fichas de la derecha, si hay.
			
			return


def combinaciones(longitud, lista):
	'''
		Genera todas las combinaciones de m en n numeros, donde m = longitud.
	'''
	
	grupo = [] # Grupo de combinaciones.
	fichas = list(range(longitud)) # Fichas en las primeras n posiciones.
	fin = list(range(len(lista) - (longitud), len(lista))) # Ultimas n posiciones (condicion de parada).
	print('Combinaciones de:', longitud)
	
	# Generacion de un grupo de combinaciones.
	while(True):
		
		# Se forma una combinacion segun las posiciones de las fichas.
		comb = comb = [lista[fichas[x]] for x in range(len(fichas))]
		grupo.append(comb) # Se agrega la combinacion al grupo actual.
		print(comb)
		
		# Las posiciones de las fichas son iguales a las posiciones finales?
		if fichas == fin:
			
			break # Termina con un grupo de combinaciones.
		
		moverFicha(fichas, lista) # Mover una ficha.
	
	return grupo


def todasCombinaciones(lista):
	'''
		Genera todas las posibles combinaciones de una lista,
		segun una longitud que va de 1 a len(lista).
	'''

	print('Lista:', lista)
	print('-' * 40)
	grupos_lons = list(range(0, len(lista) + 1)) # Longitudes de cada grupo.
	grupos = [] # Lista de grupos de combinaciones.

	# Formacion de las combinaciones.
	for grupo_lon in grupos_lons:
		
		grupo = combinaciones(grupo_lon, lista)
		grupos.append(grupo)
		print('-' * 30)
	
	return grupos


if __name__ == '__main__':

	print('Combinaciones de m elementos en n elementos')
	lista = [1, 2, 3, 4, 5,  6, 7]
	combinaciones = todasCombinaciones(lista)
	print()
	resumen(combinaciones)
