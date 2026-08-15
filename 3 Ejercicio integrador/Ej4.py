# ============================================================
# EJERCICIO 4 — "Escape Room: La Bóveda"
# ============================================================
# Historia:
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía
# y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin
# energía o sin tiempo, ganás.
#
# Variables iniciales (NO se piden por teclado):
# - energia = 100
# - tiempo = 12
# - cerraduras_abiertas = 0
# - alarma = False
# - codigo_parcial = ""
#

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""



# Validaciones obligatorias:
# - No usar try/except
# - Pedir nombre del agente y validar con .isalpha() en un while

agente = input("Ingrese su nombre: ")

while not agente.isalpha():
    print("No ha ingresado un nombre valido")
    agente = input("Ingrese su nombre: ")

# - Validar opciones del menú y cualquier número pedido con .isdigit() en
#   un while
# - El juego debe funcionar con estructuras secuenciales, condicionales y
#   repetitivas (puede usar .lower(), len(), formateo, etc.)
#
# Regla anti-spam (muy importante):
# Para evitar que el jugador gane eligiendo "Forzar cerradura" 3 veces
# seguidas al iniciar:
# - Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas:
#   - se cobra el costo normal (-20 energía, -2 tiempo)
#   - NO abre cerradura
#   - se activa la alarma automáticamente (alarma = True) porque
#     "la cerradura se trabó"
# - Si el jugador elige opción 2 o 3, se corta la racha de "forzar seguidas"
#
# Menú de acciones (se repite mientras el juego siga):
# El juego continúa mientras:
# - energia > 0, tiempo > 0, cerraduras_abiertas < 3
# - y no esté bloqueado por alarma
#
# En cada turno mostrar el estado y el siguiente menú:
# 1) Forzar cerradura (costo: -20 energía, -2 tiempo)
#    - Si la energía está por debajo de 40, hay "riesgo de alarma":
#      pedir un número 1-3 (validado). Si elige 3 -> alarma=True
#    - Si no hay alarma, abre 1 cerradura
#    - Regla anti-spam: si es la 3ra vez seguida forzando, se activa
#      alarma y no abre

forzar_cerradura = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:
    opcion = input("\nMenu:\n1) Forzar cerradura  \n2) Hackear panel  \n3) Descansar\n \nOpcion: ")
    while not opcion.isdigit() or (int(opcion)<1 or int(opcion)>3):
        print("Error, ha elegido una opcion no valida")
        opcion = input("Ingrese una opcion valida: ")
    if opcion == "1":
        forzar_cerradura += 1
        energia -= 20
        tiempo -= 2
        if forzar_cerradura == 3:
            alarma = True
        elif energia < 40:
            numero_pedido = input("Elija un numero de 1 a 3: ")
            while not numero_pedido.isdigit() or int(numero_pedido)<1 or int(numero_pedido)>3:
                print("Entrada invalida")
                numero_pedido = input("Ingrese un numero de 1 a 3: ")
            if numero_pedido == "3":
                alarma = True
            else: 
                cerraduras_abiertas += 1
        else:
            cerraduras_abiertas += 1

# 2) Hackear panel (costo: -10 energía, -3 tiempo)
#    - Debe usar un for de 4 pasos mostrando progreso
#    - En cada paso sumar una letra al codigo_parcial (por ejemplo "A")
#    - Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si
#      todavía faltan
    if opcion == "2":
        forzar_cerradura = 0
        energia -= 10
        tiempo -= 3
        for i in range(4):
            codigo_parcial += "A"
            print(f"Intentando combinaciones: {codigo_parcial}")
        if len(codigo_parcial)>=8 and cerraduras_abiertas<3:
            cerraduras_abiertas += 1
            codigo_parcial = ""

# 3) Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON:
#    -10 energía extra)
    if opcion == "3":
        forzar_cerradura = 0
        energia += 15
        if energia > 100:
            energia = 100
        if alarma == True:
            energia -= 10
        tiempo -= 1

if cerraduras_abiertas == 3:
    print("VICTORIA: Has abierto la boveda")
elif alarma and tiempo <= 3:
    print("Sistema bloqueado por alarma")
elif energia <= 0 or tiempo <=0:
    print("DERROTA: Boveda cerrada")
else:
    print("Has forzado la cerradura muchas veces seguidas. Saliendo del sistema ... ... ...")

#
# Regla de bloqueo por alarma:
# - Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el
#   sistema se bloquea y se pierde
#
# Condiciones de fin:
# - Si cerraduras_abiertas == 3 -> VICTORIA
# - Si energia <= 0 o tiempo <= 0 -> DERROTA
# - Si se bloquea por alarma -> DERROTA (bloqueo)
