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
         'A': -4000, 
         'B': -9000, 
         'C': 34000, 
         'D': -15000, 
         'E': -10000, 
         'F': 40000, 
         'G': -7500, 
         'H': 42000, 
         'I': -5000, 
         'J':-30000
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

#Obtiene distancia de bancoActual a banco
def obtenerDistancia(bancoActual,banco):
    distFila = POS[bancoActual]
    distColumna = POS[banco]
    return DIST[distFila][distColumna]

#Obtiene el costo de visitar el banco en base a la heuristica
def obtenerCostoDelBanco(bancoActual, banco):
	return N*obtenerDistancia(bancoActual,banco)+ M*MONTO[banco]

#Define cual sera el siguiente banco a visitar
def elegirSiguienteBanco(bancoActual, dineroCamion):
	costoMin = float('inf')
	bancoMin = ''
	for banco in bancosSinVisitar:
		if (banco != bancoActual and (dineroCamion+MONTO[banco] > 0) and (dineroCamion+MONTO[banco] <= MAX_CAMION)):
			costoBanco = obtenerCostoDelBanco(bancoActual,banco)
			if (costoBanco < costoMin):
				bancoMin = banco
				costoMin = costoBanco
	return bancoMin

def agregarVueltaAlInicio(solucion,bancoActual):
    solucion.append('O')
    costo = obtenerDistancia(bancoActual,'O')

def aplicarHeuristicaDeConstruccion():
	solucion = ['O']
	bancoActual = 'O'
	dineroCamion = 0
	numeroDePaso = 1
	while (len(solucion)<len(BANCOS)):
		bancoElegido = elegirSiguienteBanco(bancoActual,dineroCamion)
		if(bancoElegido == ''):
			print('No encontro solucion')
			break
		dineroCamion += MONTO[bancoElegido]
		bancosSinVisitar.remove(bancoElegido)
		solucion.append(bancoElegido)
		bancoActual = bancoElegido
		print('Numero De Paso: '+str(numeroDePaso))   
		print('Banco Elegido: '+bancoActual)
		print('Dinero del Camion: '+str(dineroCamion)+ '\n')
		numeroDePaso += 1

	agregarVueltaAlInicio(solucion,bancoActual)
	print('Camino obtenido:')        
	print(solucion)
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

###############################################################################

main()