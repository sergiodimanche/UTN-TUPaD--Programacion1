# ============================================================
# EJERCICIO 3 — "Agenda de Turnos con Nombres (sin listas)"
# ============================================================
# Contexto:
# Hay 2 días de atención: Lunes y Martes.
# Cada día tiene cupos fijos:
# - Lunes: 4 turnos
# - Martes: 3 turnos
#
# Reglas:
# 1. Pedir nombre del operador (solo letras)

operador = input("Ingrese su nombre: ")

while not operador.isalpha():
    print("No ha ingresado un nombre valido")
    operador = input("Ingrese su nombre: ")

# 2. Menú repetitivo hasta salir:
#    1) Reservar turno
#    2) Cancelar turno (por nombre)
#    3) Ver agenda del día
#    4) Ver resumen general
#    5) Cerrar sistema

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
    opcion = input("\n1) Reservar turno  \n2) Cancelar turno (por nombre)  \n3) Ver agenda del dia  \n4) Ver resumen general \n5) Cerrar sistema\n \nOpcion: ")
    while not opcion.isdigit() or (int(opcion)<1 or int(opcion)>5):
        print("Opcion invalida")
        opcion = input("Opcion: ")
# 3. Reservar: opcion 1
#    - Elegir día (1=Lunes, 2=Martes)
#    - Pedir nombre del paciente (solo letras)
#    - Verificar que no esté repetido en ese día (comparando con las
#      variables ya cargadas)
#    - Guardar en el primer espacio libre (ej. lunes1, lunes2...)
    if opcion == "1":
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        while not nombre_paciente.isalpha():
            print("No ha ingresado un nombre valido")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
        nombre_paciente = nombre_paciente.lower()
        dia_reserva = input("Elija un dia: 1=Lunes, 2=Martes: ")
        while not dia_reserva.isdigit() or (int(dia_reserva)<1 or int(dia_reserva)>2):
            print("Dia invalido")
            dia_reserva = input("Elija un dia valido: ")
        if dia_reserva == "1":
            if lunes1 == nombre_paciente or lunes2 == nombre_paciente or lunes3 == nombre_paciente or lunes4 == nombre_paciente:
                print("El paciente ya ha reservado un turno ese mismo dia")
            else:
                if lunes1 == "":
                    print("Se le ha asignado el primer turno del dia")
                    lunes1 = nombre_paciente
                elif lunes2 == "":
                    print("Se le ha asignado el segundo turno del dia")
                    lunes2 = nombre_paciente
                elif lunes3 == "":
                    print("Se le ha asignado el tercer turno del dia")
                    lunes3 = nombre_paciente
                elif lunes4 == "":
                    print("Se le ha asignado el cuarto turno del dia")
                    lunes4 = nombre_paciente
                else:
                    print("No hay turnos disponibles en el dia")
        elif dia_reserva == "2":
            if martes1 == nombre_paciente or martes2 == nombre_paciente or martes3 == nombre_paciente:
                print("El paciente ya ha reservado un turno ese mismo dia")
            else:
                if martes1 == "":
                    print("Se le ha asignado el primer turno del dia")
                    martes1 = nombre_paciente
                elif martes2 == "":
                    print("Se le ha asignado el segundo turno del dia")
                    martes2 = nombre_paciente
                elif martes3 == "":
                    print("Se le ha asignado el tercer turno del dia")
                    martes3 = nombre_paciente
                else:
                    print("No hay turnos disponibles en el dia")
# 4. Cancelar:
#    - Elegir día
#    - Pedir nombre del paciente (solo letras)
#    - Si existe, cancelar y dejar el espacio vacío ("")
    elif opcion == "2":
        dia_cancelacion = input("Elija un dia: 1=Lunes, 2=Martes: ")
        while not dia_cancelacion.isdigit() or (int(dia_cancelacion)<1 or int(dia_cancelacion)>2):
            print("Dia invalido")
            dia_cancelacion = input("Elija un dia valido: ")
        nombre_cancelacion = input("Ingrese el nombre del paciente: ")
        while not nombre_cancelacion.isalpha():
            print("No ha ingresado un nombre valido")
            nombre_cancelacion = input("Ingrese el nombre del paciente: ")
        nombre_cancelacion = nombre_cancelacion.lower()
        if dia_cancelacion == "1":
            if lunes1 == nombre_cancelacion:
                print("Se ha cancelado el primer turno del dia Lunes")
                lunes1 = ""
            elif lunes2 == nombre_cancelacion:
                print("Se ha cancelado el segundo turno del dia Lunes")
                lunes2 = ""
            elif lunes3 == nombre_cancelacion:
                print("Se ha cancelado el tercer turno del dia Lunes")
                lunes3 = ""
            elif lunes4 == nombre_cancelacion:
                print("Se ha cancelado el cuarto turno del dia Lunes")
                lunes4 = ""
            else:
                print("No se han encontrado turnos por cancelar el dia Lunes")
        elif dia_cancelacion == "2":
            if martes1 == nombre_cancelacion:
                print("Se ha cancelado el primer turno del dia Martes")
                martes1 = ""
            elif martes2 == nombre_cancelacion:
                print("Se ha cancelado el segundo turno del dia Martes")
                martes2 = ""
            elif martes3 == nombre_cancelacion:
                print("Se ha cancelado el tercer turno del dia Martes")
                martes3 = ""
            else:
                print("No se han encontrado turnos por cancelar el dia Martes")
# 5. Ver agenda del día:
#    - Mostrar los turnos del día en orden (Turno 1..N), indicando "(libre)"
#      si está vacío
    elif opcion == "3":
        dia_agenda = input("Elija un dia: 1=Lunes, 2=Martes: ")
        while not dia_agenda.isdigit() or (int(dia_agenda)<1 or int(dia_agenda)>2):
            print("Dia invalido")
            dia_agenda = input("Elija un dia valido: ")
        if dia_agenda == "1":
            if lunes1 != "":
                print(f"Turno 1: {lunes1}")
            else:
                print("Turno 1: (Libre)")
            if lunes2 != "":
                print(f"Turno 2: {lunes2}")
            else:
                print("Turno 2: (Libre)")
            if lunes3 != "":
                print(f"Turno 3: {lunes3}")
            else:
                print("Turno 3: (Libre)")
            if lunes4 != "":
                print(f"Turno 4: {lunes4}")
            else:
                print("Turno 4: (Libre)")
        elif dia_agenda == "2":
            if martes1 != "":
                print(f"Turno 1: {martes1}")
            else:
                print("Turno 1: (Libre)")
            if martes2 != "":
                print(f"Turno 2: {martes2}")
            else:
                print("Turno 2: (Libre)")
            if martes3 != "":
                print(f"Turno 3: {martes3}")
            else:
                print("Turno 3: (Libre)")
# 6. Resumen general:
#    - Turnos ocupados y disponibles por día
#    - Día con más turnos (o empate)
    elif opcion == "4":
        contador_lunes_libres = 0
        contador_martes_libres = 0
        if lunes1 == "":
            contador_lunes_libres += 1
        if lunes2 == "":
            contador_lunes_libres += 1
        if lunes3 == "":
            contador_lunes_libres += 1
        if lunes4 == "":
            contador_lunes_libres += 1
        if martes1 == "":
            contador_martes_libres += 1
        if martes2 == "":
            contador_martes_libres += 1
        if martes3 == "":
            contador_martes_libres += 1
        print(f"El dia lunes hay {contador_lunes_libres} turnos libres y {4-contador_lunes_libres} turnos ocupados")
        print(f"El dia martes hay {contador_martes_libres} turnos libres y {3-contador_martes_libres} turnos ocupados")
        ocupados_lunes = 4 - contador_lunes_libres
        ocupados_martes = 3 - contador_martes_libres
        if ocupados_lunes > ocupados_martes:
            print("El dia con mas turnos ocupados es el Lunes")
        elif ocupados_lunes < ocupados_martes:
            print("El dia con mas turnos ocupados es el Martes")
        else:
            print("Lunes y Martes tienen la misma cantidad de turnos ocupados")
    elif opcion == "5":
        print("Cerrando sistema ... ... ...")
        break

#
# Restricciones:
# - No listas, no diccionarios, no sets, no tuplas
# - Se permite usar "" como "vacío"
# - Validaciones con .isalpha() y .isdigit() (sin try/except)
