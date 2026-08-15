# ============================================================
# EJERCICIO 5 — "Escape Room: La Arena del Gladiador"
# ============================================================
# 1. Descripción del Escenario:
# Simulador de batalla por turnos. El programa enfrenta a un usuario
# (Gladiador) contra un oponente controlado por la computadora (Enemigo).
# Objetivo: reducir los HP del oponente a cero antes de que él lo haga con vos.
# Evalúa: variables (int, float, string, boolean), estructuras de control
# (if/elif/else), ciclos (while y for) y validación de datos estricta.
#
# 2. Requerimientos técnicos:
# A. Tipos de datos obligatorios:
#    - String: nombre del jugador
#    - Int: Puntos de Vida (HP) y cantidad de pociones
#    - Float: cálculo del daño (golpe crítico multiplica el ataque por 1.5)
#    - Boolean: para controlar si el juego sigue activo o quién tiene el turno
#
# B. Reglas de validación:
#    - No está permitido usar try/except
#    - Para validar texto: .isalpha() dentro de un ciclo while
#    - Para validar números: .isdigit() dentro de un ciclo while
#
# 3. Flujo del programa:
#
# Paso 1: Configuración del personaje
# - Pedir nombre del Gladiador
# - Validación: solo letras. Si ingresa números, símbolos o lo deja vacío,
#   mostrar "Error: Solo se permiten letras" y volver a preguntar

nombre_gladiadior = input("--- BIENVENIDO A LA ARENA ---\nNombre del Gladiador: ")
while not nombre_gladiadior.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiadior = input("Por favor, vuelva a ingresar el nombre correctamente: ")



# Paso 2: Inicialización de estadísticas (NO se preguntan al usuario)
# - Vida del Gladiador: 100 (int)
# - Vida del Enemigo: 100 (int)
# - Pociones de Vida: 3 (int)
# - Daño base "Ataque Pesado": 15 (int)
# - Daño base del enemigo: 12 (int)
# - Turno Gladiador: True (booleano)

vida_del_gladiador = 100
vida_del_enemigo = 100
pociones_de_vida = 3
ataque_pesado = 15
daño_enemigo = 12
turno_gladiador = True #variable que finalmente no use. No encontre el motivo del pedido de esta variable.

#
# Paso 3: El ciclo de combate
# El juego entra en un ciclo que se repite MIENTRAS ambos combatientes
# tengan más de 0 puntos de vida.
#
# Turno del jugador:
# - Muestra vida actual de ambos y pociones restantes
# - Ofrece un menú con 3 opciones:
#   1) Ataque Pesado
#   2) Ráfaga Veloz (requiere uso de for)
#   3) Curar
# - Validación del menú: debe ser número (.isdigit()) y debe ser 1, 2 o 3.
#   Si falla, mostrar error y volver a pedir.
#

while vida_del_gladiador>0 and vida_del_enemigo>0:
    print(f"""=== INICIO DEL COMBATE === 
{nombre_gladiadior} (HP: {vida_del_gladiador}) vs Enemigo (HP: {vida_del_enemigo}) | Pociones: {pociones_de_vida}""")
    opcion = input("Elige accion:\n1) Ataque Pesado \n2) Rafaga Veloz \n3) Curar \nOpcion: ")
    while not opcion.isdigit() or (int(opcion)<1 or int(opcion)>3):
        print("Error: Ingrese un número válido")
        opcion = input("Opcion: ")

# Lógica de las acciones:
#
# Acción A: Ataque Pesado (Opción 1)
# - Calcula el daño final. Si la vida del enemigo es menor a 20 puntos,
#   el jugador realiza un "Golpe Crítico" multiplicando su daño base por
#   1.5 (resultado float)
# - Resta el daño a la vida del enemigo
# - Muestra: "¡Atacaste al enemigo por X puntos de daño!"

    if opcion == "1":
        if vida_del_enemigo<20:
            print("Golpe critico!")
            daño = ataque_pesado * 1.5
        else:
            print("Ataque pesado")
            daño = ataque_pesado
        vida_del_enemigo = vida_del_enemigo - daño
        print(f"¡Atacaste al enemigo por {daño} puntos de daño!")

# Acción B: Ráfaga Veloz (Opción 2)
# - Requiere un bucle for, se repite 3 veces (usando range)
# - En cada repetición:
#   1. Resta 5 puntos de daño a la vida del enemigo
#   2. Muestra: "> Golpe conectado por 5 de daño"

    if opcion == "2":
        print(">>¡Inicias una ráfaga de golpes!")
        for i in range(3):
            print("> Golpe conectado por 5 de daño")
            vida_del_enemigo -= 5


# Acción C: Curar (Opción 3)
# - Si tiene pociones (> 0): suma 30 puntos a su vida y resta 1 poción
# - Si NO tiene pociones: muestra "¡No quedan pociones!" y pierde el turno
#   (el enemigo ataca igual)

    if opcion == "3":
        if pociones_de_vida > 0:
            vida_del_gladiador += 30
            pociones_de_vida -= 1
        elif pociones_de_vida == 0:
            print("¡No quedan pociones!")

# Turno del enemigo:
# - Justo después de la acción del jugador, el enemigo ataca automáticamente
# - Resta el daño base del enemigo (12) a la vida del jugador
# - Muestra: "¡El enemigo te atacó por 12 puntos de daño!"
    if vida_del_enemigo>0: 
        print(">> ¡El enemigo contraataca por 12 puntos!")
        vida_del_gladiador -= 12

#
# Paso 4: Fin del juego
# Cuando el ciclo termine (la vida de alguno llegó a 0 o menos):
# - Si vida_jugador > 0: mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
# - Si vida_jugador <= 0: mostrar "DERROTA. Has caído en combate."

if vida_del_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiadior} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")


# Ejemplo de ejecución (consola):
# --- BIENVENIDO A LA ARENA ---
# Nombre del Gladiador: Leonidas1
# Error: Solo se permiten letras.
# Nombre del Gladiador: Leonidas
# === INICIO DEL COMBATE ===
# Leonidas (HP: 100) vs Enemigo (HP: 100) | Pociones: 3
# Elige acción:
# 1. Ataque Pesado
# 2. Ráfaga Veloz
# 3. Curar
# Opción: A
# Error: Ingrese un número válido.
# Opción: 2
# >> ¡Inicias una ráfaga de golpes!
# > Golpe conectado por 5 de daño
# > Golpe conectado por 5 de daño
# > Golpe conectado por 5 de daño
# >> ¡El enemigo contraataca por 12 puntos!
# === NUEVO TURNO ===
# Leonidas (HP: 88) vs Enemigo (HP: 85) | Pociones: 3
# ...