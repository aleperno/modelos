import numpy as np

################################## Parametros ##################################

# Maximo Camion
MAX_CAMION = 50000

# Variables de peso
M = 1
N = 1

##################################### Data #####################################

# Declaro los bancos. Considero 'O' como el inicial
# Central                  O
# Banco Portenio           A   
# Banco Del Plata          B
# Banco De Los Andres      C
# Banco Plural             D
# Banco Del Norte          E
# Banco Pampeano           F
# Banco Cooperativo        G
# Banco Sol                H
# Banco Republica          I
# Banco Vientos del Sur    J

BANCOS = ['O', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

MONTO = {'O': 0, 
         'A': -44036, 
         'B': -9025, 
         'C': 34580, 
         'D': -46829, 
         'E': -16677, 
         'F': 37619, 
         'G': 48998, 
         'H': 42037, 
         'I': -5090, 
         'J':-33475
        }

POS = {'O':0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,'G': 7, 'H': 8, 'I': 9, 'J': 10}

DIST = [[0, 4, 8, 4, 1, 4, 4, 7, 2, 1, 6],
		[4, 0, 4, 4, 8, 7, 4, 9, 7, 5, 9],
		[8, 4, 0, 1, 9, 3, 8, 4, 5, 1, 6],
		[4, 4, 1, 0, 5, 3, 3, 4, 4, 6, 1],
		[1, 8, 9, 5, 0, 8, 2, 1, 6, 3, 1],
		[4, 7, 3, 3, 8, 0, 6, 8, 7, 2, 8],
		[4, 4, 8, 3, 2, 6, 0, 1, 1, 6, 8],
		[7, 9, 4, 4, 1, 8, 1, 0, 7, 2, 4],
		[2, 7, 5, 4, 6, 7, 1, 7, 0, 5, 3],
		[1, 5, 1, 6, 3, 2, 6, 2, 5, 0, 6],
		[6, 9, 6, 1, 1, 8, 8, 4, 3, 6, 0]]

bancosVisitados = ['O']
bancosSinVisitar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
costoTotalDelViaje = 0

################################ Resolucion ####################################

def obtenerCostoDelBanco(bancoActual, banco, dineroCamion):
    distancia = obtenerDistancia(bancoActual,banco)
    montoRestante,dineroCamion = obtenerMontoRestante(dineroCamion,banco)
    costo = obtenerCostoTotal(distancia,montoRestante)
    return costo

def elegirSiguienteBanco(bancoActual, dineroCamion):
	costoMin = float('inf')
	bancoMin = ''
	for banco in bancosSinVisitar:
		if (banco != bancoActual and (dineroCamion+MONTO[banco] > 0) and (dineroCamion+MONTO[banco] <= MAX_CAMION)):
			costoBanco = obtenerCostoDelBanco(bancoActual,banco,dineroCamion)
			if (costoBanco < costoMin):
				bancoMin = banco
				costoMin = costoBanco
	global costoTotalDelViaje
	costoTotalDelViaje += costoMin
	return bancoMin

def aplicarHeuristicaDeConstruccion():
	solucion = ['O']
	bancoActual = 'O'
	dineroCamion = 0
	numeroDePaso = 1


	while (len(solucion)<len(bancos)):
		bancoElegido = elegirSiguienteBanco(bancoActual,dineroCamion)
		dineroCamion += MONTO[bancoElegido]
		visitarBanco(bancoElegido)
		bancosSinVisitar.remove(bancoElegido)
		solucionConstruccion.append(bancoElegido)
		bancoActual = bancoElegido
		print('Numero De Paso: '+str(numeroDePaso))   
		print('Banco Elegido: '+bancoActual)
		print('Dinero del Camion: '+str(dineroCamion)+ '\n')
		numeroDePaso += 1


	agregarVueltaAlInicio(bancoActual)
	print('Camino obtenido:')        
	print(bancosVisitados)
	print('Costo total del viaje obtenido:')        
	print(costoTotalDelViaje)


	return solucion

def aplicarHeuristicaDeMejoramiento(solucionOpcional):
	solucion = []
	return solucion

def main( ):
	print("Tp presentacion final modelos y optimizacion 1\n")
	solucionConstruccion = aplicarHeuristicaDeConstruccion()
	aplicarHeuristicaDeMejoramiento(solucionConstruccion)
