# ============================================================
# EJERCICIO 1 — "Caja del Kiosco"
# ============================================================
# Objetivo: Simular una compra con validaciones y cálculo de total.
#
# Requisitos:
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while)
#    - No aceptar vacío en nombre (si queda vacío, es error)

nombre = input("Por favor, ingrese el nombre del cliente: ")

while not nombre.isalpha():
    print("No ha ingresado un nombre valido.")
    nombre = input("Por favor, ingrese el nombre del cliente: ")

# 2. Pedir cantidad de productos a comprar (entero positivo, validar con
#    .isdigit() en while)
#    - Cantidad > 0 (si ingresa 0, volver a pedir)

cantidad_productos = input("Por favor, ingrese la cantidad de productos a comprar: ")

while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("Ha igresado una cantidad invalida.")
    cantidad_productos = input("Por favor, ingrese una cantidad de productos valida: ")

# 3. Por cada producto (usar for):
#    - Pedir precio (entero, validar .isdigit())
#    - Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#      cualquier mayúscula/minúscula)
#    - Si tiene descuento: aplicar 10% al precio de ese producto

cantidad_productos = int(cantidad_productos)
total_productos = 0
total_ahorro = 0

for i in range(1, cantidad_productos+1):
    precio_producto = input("Ingreso el precio del producto numero "+str(i)+": ")
    while not precio_producto.isdigit():
        precio_producto = input("Ha ingresado un precio invalido, por favor ingrese nuevamente el precio: ")
    precio_producto = int(precio_producto)

    tiene_descuento = input("Indique si el producto tiene descuento (s/n): ")
    while tiene_descuento.lower() != "s" and tiene_descuento.lower() != "n":
        tiene_descuento = input("Ha ingresado un dato erroneo, por favor ingrese si el producto tiene descuento: ")
    tiene_descuento = tiene_descuento.lower()

    if tiene_descuento == "s":
        ahorro = precio_producto * 0.10
        total_ahorro += ahorro

    total_productos += precio_producto

# 4. Al final mostrar:
#    - Total sin descuentos
#    - Total con descuentos
#    - Ahorro total
#    - Promedio por producto (usar float, formatear con :.2f)

total_condescuento = total_productos - total_ahorro
promedio_por_producto = (total_condescuento/cantidad_productos)

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"El importe total sin descuentos es de ${total_productos:.2f}")
print(f"El importe total con descuentos es de ${total_condescuento:.2f}")
print(f"Ahorro: ${total_ahorro:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")
#
# Validaciones obligatorias:
# - Sin try/except
#
# Salida esperada (ejemplo):
# Cliente: Ana
# Cantidad de productos: 3
# Producto 1 - Precio: 100   Descuento (S/N): s
# Producto 2 - Precio: 50    Descuento (S/N): n
# Producto 3 - Precio: 200   Descuento (S/N): s
#
# Total sin descuentos: $350
# Total con descuentos: $320.00
# Ahorro: $30.00
# Promedio por producto: $106.67
