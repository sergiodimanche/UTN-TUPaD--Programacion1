# ============================================================
# Ejercicio A — "Boletería de Cine"
# ============================================================
# Objetivo: Simular la venta de entradas de una función de cine
# con precios según edad y combos opcionales.
#
# Requisitos:
# 1. Pedir nombre del operador de boletería (solo letras, validar con .isalpha() en while).

nombre = input("Por favor, ingrese su nombre: ")
while not nombre.isalpha():
    print("Error: El nombre del operador debe contener solo letras.")
    nombre = input("Por favor, ingrese su nombre: ")


# 2. Pedir cantidad de entradas a vender (entero positivo, validar con .isdigit() en while;
#    si ingresa 0, volver a pedir).

cantidad_entradas = input("Ingrese la cantidad de entradas a vender: ")
while not cantidad_entradas.isdigit() or int(cantidad_entradas) <= 0:
    print("Error: La cantidad de entradas debe ser un número entero positivo.")
    cantidad_entradas = input("Ingrese la cantidad de entradas a vender: ")
cantidad_entradas = int(cantidad_entradas)

# 3. Por cada entrada (usar for):
#    - Pedir edad del espectador (validar .isdigit()).
#    - Calcular el precio según la edad:
#        Menor de 12 años: $1500 (entrada niño)
#        Entre 12 y 64 años: $3000 (entrada general)
#        65 años o más: $1800 (entrada jubilado)
#    - Preguntar si quiere agregar combo pochoclos+gaseosa (S/N, validar en while,
#      aceptar cualquier mayúscula/minúscula). Si acepta, sumar $2200 al precio de esa entrada.
# 4. Al finalizar la venta de todas las entradas, mostrar:
#    - Total de entradas vendidas
#    - Cantidad de entradas por categoría (niño, general, jubilado)
#    - Cantidad de combos vendidos
#    - Recaudación total (usar float, formatear con :.2f)
#    - Precio promedio por entrada
#
# Validaciones obligatorias:
# - Sin try/except.
# - Nombre del operador no puede quedar vacío.
# - Edad no puede ser negativa (si el usuario ingresa un número negativo, se considera
#   inválido y se debe volver a pedir).
#
# Salida esperada (ejemplo):
# Operador: Marcos
# Cantidad de entradas: 3
# Entrada 1 - Edad: 10
#  -> Entrada niño: $1500
#  Combo pochoclos+gaseosa (S/N): s
#  -> Total entrada 1: $3700
# Entrada 2 - Edad: 30
#  -> Entrada general: $3000
#  Combo pochoclos+gaseosa (S/N): n
#  -> Total entrada 2: $3000
# Entrada 3 - Edad: 70
#  -> Entrada jubilado: $1800
#  Combo pochoclos+gaseosa (S/N): s
#  -> Total entrada 3: $4000
# --- RESUMEN ---
# Entradas vendidas: 3
# Niños: 1 Generales: 1 Jubilados: 1
# Combos vendidos: 2
# Recaudación total: $10700.00
# Precio promedio por entrada: $3566.67


# ============================================================
# Ejercicio B — "Farmacia de Turno"
# ============================================================
# Objetivo: Simular la atención de una farmacia de turno con
# control de stock y validación de recetas.
#
# Requisitos:
# 1. Definir un stock inicial fijo en el código: stock = 50 unidades de un medicamento controlado.
# 2. Pedir nombre del farmacéutico (solo letras, validar con .isalpha() en while).
# 3. Mostrar un menú repetitivo (usar while) que se repite hasta que se elija "Cerrar turno":
#    1) Vender medicamento
#    2) Reponer stock
#    3) Consultar stock actual
#    4) Cerrar turno
# 4. Validar la opción elegida: debe ser numérica (.isdigit()) y estar entre 1 y 4;
#    si no, mostrar error y volver a mostrar el menú.
# 5. Vender medicamento:
#    - Pedir si el cliente presenta receta médica (S/N, validar en while).
#    - Pedir cantidad a vender (validar .isdigit()).
#    - Reglas: si NO presenta receta, no puede vender más de 2 unidades.
#      Si pide más, rechazar la venta e informar el motivo.
#    - No se puede vender más de lo que hay en stock. Si pide más, rechazar
#      e informar cuánto stock queda disponible.
#    - Si la venta es válida, descontar del stock y mostrar el stock resultante.
# 6. Reponer stock: pedir cantidad a reponer (validar .isdigit(), debe ser mayor a 0)
#    y sumarla al stock.
# 7. Consultar stock: mostrar el stock actual.
# 8. Al cerrar turno, mostrar un resumen con: total de unidades vendidas en el turno,
#    total de ventas rechazadas (por cualquier motivo) y stock final.
#
# Validaciones obligatorias:
# - Sin try/except.
# - Nombre del farmacéutico no puede quedar vacío.
# - Cantidad a vender o reponer debe ser mayor a 0 (si ingresa 0, se considera inválido).
#
# Salida esperada (ejemplo):
# Farmacéutico: Laura
# 1) Vender 2) Reponer 3) Consultar stock 4) Cerrar turno
# Opción: 1
# ¿Presenta receta? (S/N): n
# Cantidad a vender: 3
# Error: sin receta solo se pueden vender hasta 2 unidades. Venta rechazada.
# Opción: 1
# ¿Presenta receta? (S/N): s
# Cantidad a vender: 5
# Venta realizada. Stock restante: 45
# Opción: 4
# --- CIERRE DE TURNO ---
# Unidades vendidas: 5
# Ventas rechazadas: 1
# Stock final: 45


# ============================================================
# Ejercicio C — "Estacionamiento Medido"
# ============================================================
# Objetivo: Simular el cobro de un estacionamiento por tiempo,
# con tarifas diferenciadas y control de vehículos.
#
# Requisitos:
# 1. Pedir cantidad de vehículos a procesar en el turno (entero positivo, validar .isdigit()
#    en while; si es 0, volver a pedir).
# 2. Por cada vehículo (usar for):
#    - Pedir patente (solo letras y números, sin validación especial más allá de que no quede vacía).
#    - Pedir tipo de vehículo: 1 = Auto, 2 = Moto, 3 = Camioneta (validar con .isdigit()
#      en while que esté entre 1 y 3).
#    - Pedir cantidad de horas estacionado (entero positivo, validar .isdigit(); si es 0,
#      volver a pedir).
#    - Calcular el costo según tarifa por hora: Auto $800/hora, Moto $500/hora, Camioneta $1000/hora.
#    - Si el vehículo estuvo estacionado más de 5 horas, aplicar un 15% de descuento sobre
#      el total de ese vehículo (por "tarifa larga estadía").
# 3. Al finalizar de procesar todos los vehículos, mostrar:
#    - Cantidad de vehículos por tipo (autos, motos, camionetas)
#    - Cantidad de vehículos que accedieron al descuento por larga estadía
#    - Recaudación total sin descuentos
#    - Recaudación total con descuentos aplicados
#    - Total ahorrado por los clientes (usar float, formatear con :.2f)
#
# Validaciones obligatorias:
# - Sin try/except.
# - Patente no puede quedar vacía.
# - Horas estacionado > 0.
#
# Salida esperada (ejemplo):
# Cantidad de vehículos: 2
# Vehículo 1
# Patente: AB123CD
# Tipo (1-Auto 2-Moto 3-Camioneta): 1
# Horas estacionado: 6
# -> Tarifa larga estadía aplicada (15% off)
# -> Total: $4080.00
# Vehículo 2
# Patente: XY456
# Tipo (1-Auto 2-Moto 3-Camioneta): 2
# Horas estacionado: 2
# -> Total: $1000.00
# --- RESUMEN DEL TURNO ---
# Autos: 1 Motos: 1 Camionetas: 0
# Vehículos con descuento: 1
# Recaudación sin descuentos: $5800.00
# Recaudación con descuentos: $5080.00
# Ahorro total de clientes: $720.00