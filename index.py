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

MONTO = {'O': 0, 'A': -44036, 'B': -9025, 'C': 34580, 'D': -46829, 'E': -16677, 'F': 37619, 'G': 48998, 'H': 42037, 'I': -5090, 'J':-33475}

POS = {'O':0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,'G': 7, 'H': 8, 'I': 9, 'J': 10}

DIST = np.matrix('0, 4, 8, 4, 1, 4, 4, 7, 2, 1, 6;4, 0, 4, 4, 8, 7, 4, 9, 7, 5, 9;8, 4, 0, 1, 9, 3, 8, 4, 5, 1, 6;4, 4, 1, 0, 5, 3, 3, 4, 4, 6, 1;1, 8, 9, 5, 0, 8, 2, 1, 6, 3, 1;4, 7, 3, 3, 8, 0, 6, 8, 7, 2, 8;4, 4, 8, 3, 2, 6, 0, 1, 1, 6, 8;7, 9, 4, 4, 1, 8, 1, 0, 7, 2, 4;2, 7, 5, 4, 6, 7, 1, 7, 0, 5, 3;1, 5, 1, 6, 3, 2, 6, 2, 5, 0, 6;6, 9, 6, 1, 1, 8, 8, 4, 3, 6, 0')

bancosVisitados = ['O']
bancosSinVisitar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
costoTotalDelViaje = 0

def main( ):
    print("Tp presentacion final modelos y optimizacion 1\n")
    solucionConstruccion = aplicarHeuristicaDeConstruccion()
    aplicarHeuristicaDeMejoramiento(solucionConstruccion)

def aplicarHeuristicaDeMejoramiento(solucionAlternativa):
    print(calcularCostoCamino(solucionAlternativa))
    return 0

def calcularCostoCamino(camino):
    costo = 0
    for banco in range(1, len(camino)-1):
        costo += obtenerDistancia(camino[banco-1], camino[banco])
    return costo

def aplicarHeuristicaDeConstruccion():    
    bancoActual = 'O'
    dineroCamion = 0
    numeroDePaso = 1
    global costoTotalDelViaje
    while (len(bancosSinVisitar)>0):
        bancoElegido = elegirSiguienteBanco(bancoActual,dineroCamion)
        dineroCamion = actulizarDineroCamion(dineroCamion,bancoElegido)
        visitarBanco(bancoElegido)
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
    return bancosVisitados

def agregarVueltaAlInicio(bancoActual):
    global costoTotalDelViaje
    bancosVisitados.append('O')
    costo = obtenerDistancia(bancoActual,'O')
    costoTotalDelViaje += costo

#Actualiza el dinero que portara el camion al visitar un banco
def actulizarDineroCamion(dineroCamion,bancoElegido):
    montoRestante,dineroCamionActualizado = obtenerMontoRestante(dineroCamion,bancoElegido)
    return dineroCamionActualizado

#Define cual sera el siguiente banco a visitar
def elegirSiguienteBanco(bancoActual,dineroCamion):
    costoMin = float('inf')
    bancoMin = ''
    for banco in bancosSinVisitar:
        if (banco != bancoActual):
            costoBanco = obtenerCostoDelBanco(bancoActual,banco,dineroCamion)
            if (costoBanco < costoMin):
                bancoMin = banco
                costoMin = costoBanco
    global costoTotalDelViaje
    costoTotalDelViaje += costoMin
    return bancoMin

def obtenerCostoDelBanco(bancoActual,banco,dineroCamion):
    distancia = obtenerDistancia(bancoActual,banco)
    montoRestante,dineroCamion = obtenerMontoRestante(dineroCamion,banco)
    costo = obtenerCostoTotal(distancia,montoRestante)
    return costo

def obtenerDistancia(bancoActual,banco):
    distFila = POS[bancoActual]
    distColumna = POS[banco]
    return (DIST[distFila,distColumna])

def obtenerMontoRestante(dineroCamion,banco):
    dineroDelBanco = MONTO[banco]
    suma = dineroCamion + dineroDelBanco
    if suma > MAX_CAMION:
        resto = suma - MAX_CAMION
        dineroCamion = MAX_CAMION
    elif suma < 0:
        resto = -suma
        dineroCamion = 0
    else:
        resto = 0
        dineroCamion = suma
    return resto,dineroCamion

#obtiene el costo definido por la formula de la heuristica
def obtenerCostoTotal(distancia,montoRestante):
    return (N*distancia+M*montoRestante)

#Mueve un banco de sin visitar a visitado
def visitarBanco(banco):
    bancosSinVisitar.remove(banco)
    bancosVisitados.append(banco)

main()
