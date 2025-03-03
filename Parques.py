import random

# Matrices de representación de los tableros
matriz_j1 = [
    ["0", "0", "0", "0", "0", "0", "0", "46", "45", "44", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "47", "0", "43", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "48", "0", "42", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "49", "0", "41", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "50", "0", "40", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "51", "0", "39", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "52", "0", "38", "0", "0", "0", "0", "0", "0", "0"],
    ["59", "58", "57", "56", "55", "54", "53", "0", "0", "0", "37", "36", "35", "34", "33", "32", "31"],
    ["60", "61", "62", "63", "64", "65", "66", "67", "68", "0", "0", "0", "0", "0", "0", "0", "30"],
    ["1", "2", "3", "4", "5", "6", "7", "0", "0", "0", "23", "24", "25", "26", "27", "28", "29"],
    ["0", "0", "0", "0", "0", "0", "0", "8", "0", "22", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "9", "0", "21", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "10", "0", "20", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "11", "0", "19", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "12", "0", "18", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "13", "0", "17", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "14", "15", "16", "0", "0", "0", "0", "0", "0", "0"]
]

matriz_j2 = [
    ["0", "0", "0", "0", "0", "0", "0", "76", "75", "74", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "77", "0", "73", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "78", "0", "72", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "79", "0", "71", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "80", "0", "70", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "81", "0", "69", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "82", "0", "68", "0", "0", "0", "0", "0", "0", "0"],
    ["89", "88", "87", "86", "85", "84", "83", "0", "0", "0", "67", "66", "65", "64", "63", "62", "61"],
    ["90", "91", "92", "93", "94", "95", "96", "97", "98", "0", "0", "0", "0", "0", "0", "0", "60"],
    ["31", "32", "33", "34", "35", "36", "37", "0", "0", "0", "53", "54", "55", "56", "57", "58", "59"],
    ["0", "0", "0", "0", "0", "0", "0", "38", "0", "52", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "39", "0", "51", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "40", "0", "50", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "41", "0", "49", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "42", "0", "48", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "43", "0", "47", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "44", "45", "46", "0", "0", "0", "0", "0", "0", "0"]
]

# Diccionario del tablero de 97 posiciones 
tablero = {str(i): str(i) for i in range(1, 98)}

# Posiciones importantes
salida = {1: 5, 2: 35}
llegada = {1: 68, 2: 98}
seguros = {1: [10, 15, 60], 2: [35, 40, 85]}

# Estado inicial de los jugadores ('bonus' para movimientos extra)
jugadores = {
    1: {
        'fichas': {'F1': None, 'F2': None, 'F3': None, 'F4': None},
        'carcel': 4,
        'salida': 0,
        'llegada': 0,
        'primera_salida': {'F1': False, 'F2': False, 'F3': False, 'F4': False},
        'bonus': 0
    },
    2: {
        'fichas': {'G1': None, 'G2': None, 'G3': None, 'G4': None},
        'carcel': 4,
        'salida': 0,
        'llegada': 0,
        'primera_salida': {'G1': False, 'G2': False, 'G3': False, 'G4': False},
        'bonus': 0
    }
}

turno = 1  # Comienza el jugador 1

def lanzar_dados(modo='desarrollador'):
    if modo == 'real':
        return random.randint(1, 6), random.randint(1, 6)
    return int(input("Ingrese el valor del dado 1: ")), int(input("Ingrese el valor del dado 2: "))

# Función para eliminar la ficha de la casilla indicada en el tablero.
def remover_ficha_de_tablero(pos, ficha):
    contenido = tablero[str(pos)]
    if not contenido.isdigit():
        piezas = contenido.split(',')
        if ficha in piezas:
            piezas.remove(ficha)
        tablero[str(pos)] = ','.join(piezas) if piezas else str(pos)

# Agrega la ficha a la casilla indicada en el diccionario 'tablero',
# acumulando su nombre mediante una coma si ya hay otra(s) ficha(s).
def agregar_ficha_a_casilla(pos, ficha):
    key = str(pos)
    if tablero[key].isdigit():
        tablero[key] = ficha
    else:
        tablero[key] += "," + ficha

# Función para determinar si hay un bloqueo en una casilla.
def es_bloqueo(pos, contenido, jugador):

    # Se considera bloqueo si:
    #   - Hay dos o más fichas del mismo equipo.
    #   - O si hay fichas de equipos distintos en una casilla especial (salida o seguro).

    piezas = [p for p in contenido.split(',') if p and not p.isdigit()]
    if len(piezas) >= 2:
        # Bloqueo si son del mismo equipo.
        team = 1 if piezas[0].startswith("F") else 2
        if all((p.startswith("F") if team == 1 else p.startswith("G")) for p in piezas):
            return True
    # Bloqueo en casilla especial si hay fichas de distintos equipos:
    if len(piezas) >= 1:
        teams = set(1 if p.startswith("F") else 2 for p in piezas)
        if len(teams) > 1:
            if pos == salida[1] or pos in seguros[1] or pos == salida[2] or pos in seguros[2]:
                return True
    return False


# Función principal para mover una ficha en el tablero.
def mover_ficha(jugador, ficha, avance, bonus_move=False):
    datos = jugadores[jugador]
    pos_actual = datos['fichas'][ficha]
    if pos_actual is None:
        return False
    new_pos = pos_actual + avance

    # Regla 5: Se requiere movimiento exacto para llegar a la meta.
    if new_pos > llegada[jugador]:
        print("Movimiento no válido: se necesita número exacto para llegar a la meta.")
        return False

    # Regla 4: Verificar bloqueos en el trayecto.
    max_permitido = avance
    for pos in range(pos_actual + 1, new_pos + 1):
        if str(pos) in tablero:
            contenido = tablero[str(pos)]
            if not contenido.isdigit() and es_bloqueo(pos, contenido, jugador):
                max_permitido = pos - pos_actual - 1
                break
    if avance > max_permitido:
        print(f"Movimiento no válido debido a un bloqueo en el trayecto. Máximo permitido: {max_permitido} casillas.")
        return False

    # Análisis de la casilla destino:
    destino = tablero[str(new_pos)]
    if destino.isdigit():
        remover_ficha_de_tablero(pos_actual, ficha)
        datos['fichas'][ficha] = new_pos
        agregar_ficha_a_casilla(new_pos, ficha)
    else:
        piezas = destino.split(',')
        equipo_movi = jugador
        equipos_dest = [1 if p.startswith("F") else 2 for p in piezas if p and not p.isdigit()]
        es_seguro = (new_pos == salida[1] or new_pos in seguros[1] or new_pos == salida[2] or new_pos in seguros[2])
        if all(t == equipo_movi for t in equipos_dest):
            # Se forma bloqueo entre fichas del mismo equipo.
            remover_ficha_de_tablero(pos_actual, ficha)
            datos['fichas'][ficha] = new_pos
            agregar_ficha_a_casilla(new_pos, ficha)
        else:
            if es_seguro:
                # En casilla especial, fichas de equipos distintos forman bloqueo.
                remover_ficha_de_tablero(pos_actual, ficha)
                datos['fichas'][ficha] = new_pos
                agregar_ficha_a_casilla(new_pos, ficha)
            else:
                # Captura (Regla 3).
                pieza_capturada = piezas[0]
                equipo_enemigo = 1 if pieza_capturada.startswith("F") else 2
                print(f"{ficha} captura a {pieza_capturada} en la casilla {new_pos}.")
                jugadores[equipo_enemigo]['fichas'][pieza_capturada] = None
                jugadores[equipo_enemigo]['carcel'] += 1
                nuevas = [p for p in piezas if p != pieza_capturada]
                tablero[str(new_pos)] = ','.join(nuevas) if nuevas else str(new_pos)
                remover_ficha_de_tablero(pos_actual, ficha)
                datos['fichas'][ficha] = new_pos
                # Se agrega la ficha al destino usando la función auxiliar.
                agregar_ficha_a_casilla(new_pos, ficha)
                # Regla 7: Bono de 20 movimientos extra.
                datos['bonus'] += 20
                print(f"Se otorgan 20 movimientos extra a jugador {jugador} por captura.")

    # Llegar a la meta:
    if new_pos == llegada[jugador]:
        print(f"¡{ficha} ha llegado a la meta!")
        datos['salida'] -= 1
        datos['llegada'] += 1
        datos['fichas'][ficha] = None
        datos['bonus'] += 10
        print(f"Se otorgan 10 movimientos extra a jugador {jugador} por llegar a la meta.")
    return True

def jugar_turno(jugador):
    global turno 
    print(f"\n=== Turno Jugador {jugador} ===")
    datos = jugadores[jugador]
    
    # Uso obligatorio de movimientos extra pendientes (Regla 9).
    while datos.get('bonus', 0) > 0:
        bono = datos['bonus']
        print(f"Tienes un bono de {bono} movimientos extra. Debes usarlo antes de continuar.")
        ficha_seleccionada = input(f"Jugador {jugador}, elige la ficha para mover {bono} casillas: ")
        if ficha_seleccionada not in datos['fichas'] or datos['fichas'][ficha_seleccionada] is None:
            print("Ficha no válida o no está en juego.")
        else:
            if mover_ficha(jugador, ficha_seleccionada, bono, bonus_move=True):
                datos['bonus'] = 0
            else:
                print("El movimiento extra no es posible. Intenta con otra ficha.")
    
    repetir_turno = True
    movimiento_realizado = False
    while repetir_turno:
        d1, d2 = lanzar_dados()
        print(f"Dados: {d1}, {d2}")
        
        # Liberar ficha desde la cárcel (incluye excepción de Regla 2).
        if datos['carcel'] > 0 and (d1 == 5 or d2 == 5 or d1 + d2 == 5):
            ficha_lib = next((f for f, pos in datos['fichas'].items() if pos is None), None)
            if ficha_lib:
                print(f"¡{ficha_lib} sale de la cárcel!")
                dest_sal = salida[jugador]
                contenido = tablero[str(dest_sal)]
                if not contenido.isdigit():
                    piezas = contenido.split(',')
                    equipo_enemigo = 2 if jugador == 1 else 1
                    enemigo_en_salida = [p for p in piezas if (jugador == 1 and p.startswith("G")) or (jugador == 2 and p.startswith("F"))]
                    if enemigo_en_salida:
                        print(f"Capturando ficha enemiga {enemigo_en_salida[0]} en la salida.")
                        jugadores[equipo_enemigo]['fichas'][enemigo_en_salida[0]] = None
                        jugadores[equipo_enemigo]['carcel'] += 1
                        nuevas = [p for p in piezas if p != enemigo_en_salida[0]]
                        tablero[str(dest_sal)] = ','.join(nuevas) if nuevas else str(dest_sal)
                        datos['bonus'] += 20
                        print(f"Se otorgan 20 movimientos extra a jugador {jugador} por captura en salida.")
                # Liberar la ficha usando la función auxiliar.
                datos['fichas'][ficha_lib] = dest_sal
                datos['carcel'] -= 1
                datos['salida'] += 1
                datos['primera_salida'][ficha_lib] = True
                agregar_ficha_a_casilla(dest_sal, ficha_lib)
                movimiento_realizado = True
        
        # Movimiento de fichas en juego.
        fichas_activas = [f for f, pos in datos['fichas'].items() if pos is not None]
        if fichas_activas:
            ficha_sel = input(f"Jugador {jugador}, elige la ficha a mover ({'/'.join(fichas_activas)}): ")
            if ficha_sel in datos['fichas'] and datos['fichas'][ficha_sel] is not None:
                if mover_ficha(jugador, ficha_sel, d1 + d2):
                    movimiento_realizado = True
            else:
                print("Ficha no válida.")
        else:
            print("No hay fichas en juego para mover.")
        
        if not movimiento_realizado:
            print("No existe movimiento posible para ninguna ficha. Se pasa el turno.")
        
        if d1 == d2 and d1 % 2 == 0:
            print(f"¡Dados iguales y pares ({d1}, {d2})! El jugador {jugador} repite turno.")
            movimiento_realizado = False
        else:
            repetir_turno = False

    turno = 2 if turno == 1 else 1

# Devuelve un diccionario con los valores de la matriz (distintos de '0') mapeados a sus coordenadas.
def obtener_mapeo(matriz):
    return {matriz[fila][columna]: (fila, columna)
            for fila in range(len(matriz))
            for columna in range(len(matriz[fila]))
            if matriz[fila][columna] != "0"}

# Se obtienen los mapeos de las matrices de tablero
mapeo1 = obtener_mapeo(matriz_j1)
mapeo2 = obtener_mapeo(matriz_j2)

# Carga los valores de tablero_dict en la matriz manteniendo la estructura original.
def cargar_matriz(matriz, tablero_dict, mapeo):
    nueva_matriz = [fila[:] for fila in matriz]
    for key, value in tablero_dict.items():
        if key in mapeo:
            fila, columna = mapeo[key]
            nueva_matriz[fila][columna] = value
    return nueva_matriz

# Imprime la matriz de forma legible.
def imprimir_tablero(matriz):
    for fila in matriz:
        print("\t".join(fila))
    print("\n")

# Implementación del código para jugar el juego
while jugadores[1]['llegada'] < 4 and jugadores[2]['llegada'] < 4:
    jugar_turno(turno)
    
    print("Tablero general (diccionario):")
    print("=====================================")
    for pos, valor in tablero.items():
        # Casillas en la llegada
        if int(pos) in llegada.values():
            tablero[pos] = ','.join(set(valor.split(',')))
        print(f"{pos}: {tablero[pos]}")
    print("=====================================")
    matriz_j1 = cargar_matriz(matriz_j1, tablero, mapeo1)
    matriz_j2 = cargar_matriz(matriz_j2, tablero, mapeo2)
    print("Tablero Jugador 1:")
    imprimir_tablero(matriz_j1)
    print("Tablero Jugador 2:")
    imprimir_tablero(matriz_j2)

print("¡Fin del juego!")