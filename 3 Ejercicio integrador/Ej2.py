# ============================================================
# EJERCICIO 2 — "Acceso al Campus y Menú Seguro"
# ============================================================
# Objetivo: Login con intentos + menú de acciones con validación estricta.
#
# Requisitos:
# 1. Definir credenciales fijas en el código:
#    - usuario correcto: "alumno"
#    - clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave
# 3. Si falla 3 veces: mostrar "Cuenta bloqueada" y terminar
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#    1) Ver estado de inscripción (mostrar "Inscripto")
#    2) Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#    3) Mostrar mensaje motivacional (1 frase)
#    4) Salir
# 5. Validación del menú:
#    - Debe ser número (.isdigit())
#    - Debe estar entre 1 y 4
#
# Cambio de clave:
# - La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
#   rechazar
#

USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"
acceso_concedido = False

for i in range(3):
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese la contraseña: ")
    if nombre_usuario != USUARIO_CORRECTO or clave != CLAVE_CORRECTA:
        print("Error, credenciales invalidas")
    else:
        print("Acceso concedido")
        acceso_concedido = True
        while True:
            opcion = input("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir \nOpcion: ")
            while not opcion.isdigit() or (int(opcion) > 4 or int(opcion) < 1):
                if not opcion.isdigit():
                    print("Error, ingrese un numero valido")
                elif int(opcion) > 4 or int(opcion) < 1:
                    print("Error, opcion fuera de rango")
                opcion = input("Opcion: ")
            if opcion == "1":
                print("Inscripto")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                while len(nueva_clave) < 6:
                    print("Error, minimo 6 caracteres")
                    nueva_clave = input("Nueva clave: ")
                confirma_clave = input("confirme su clave: ")
                while confirma_clave != nueva_clave:
                    print("Las claves no coinciden")
                    confirma_clave = input("Vuelva a confirmar su clave: ")
                print("La clave fue actualizada exitosamente")
                CLAVE_CORRECTA = nueva_clave
            elif opcion == "3":
                print("Gracias por no pedir validaciones!")
            elif opcion == "4":
                print("Saliendo del sistema ... ... ...")
                break
        if acceso_concedido:
            break
if not acceso_concedido:
    print("Cuenta bloqueada")

# Salida esperada:
# Intento 1/3 - Usuario: alumno
# Clave: xxx
# Error: credenciales inválidas.
#
# Intento 2/3 - Usuario: alumno
# Clave: python123
# Acceso concedido.
#
# 1) Estado  2) Cambiar clave  3) Mensaje  4) Salir
# Opción: a
# Error: ingrese un número válido.
# Opción: 5
# Error: opción fuera de rango.
# Opción: 2
# Nueva clave: 123
# Error: mínimo 6 caracteres.
# ...
