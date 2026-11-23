# Prompt generado: Documentar código

Generado el 23/11/2026 a las 23:09.

Copia el texto del bloque y pégalo en tu asistente de IA.

```text
Actúa como un ingeniero de software senior especializado en documentación técnica.

CONTEXTO
Tengo el siguiente código escrito en Python. Necesito documentarlo para que lo entienda un compañero nuevo del equipo.

CÓDIGO
"""
"""
Código de ejemplo para probar el prompt "Documentar código".

Es un módulo pequeño de una tienda: calcula totales, aplica descuentos
y valida el stock. Tiene errores controlados a propósito para que la
documentación generada sea más interesante.
"""


def calcular_total(precios, descuento=0.0):
    """Suma una lista de precios y aplica un descuento porcentual."""
    if not precios:
        raise ValueError("La lista de precios no puede estar vacía")
    if descuento < 0 or descuento > 1:
        raise ValueError("El descuento debe estar entre 0 y 1")

    subtotal = sum(precios)
    return round(subtotal * (1 - descuento), 2)


def validar_stock(stock_disponible, cantidad_solicitada):
    """Devuelve True si hay suficiente stock; False si no."""
    if cantidad_solicitada <= 0:
        raise ValueError("La cantidad solicitada debe ser mayor que cero")
    return stock_disponible >= cantidad_solicitada


def resumen_compra(productos):
    """
    Recibe una lista de diccionarios con nombre, precio y cantidad.
    Devuelve un texto con el detalle y el total a pagar.
    """
    if not productos:
        return "No hay productos en la compra."

    lineas = []
    total = 0.0
    for producto in productos:
        subtotal = producto["precio"] * producto["cantidad"]
        total += subtotal
        lineas.append(
            f"{producto['cantidad']} x {producto['nombre']} = ${subtotal:,.2f}"
        )

    lineas.append(f"TOTAL: ${total:,.2f}")
    return "\n".join(lineas)


if __name__ == "__main__":
    carrito = [
        {"nombre": "Laptop Pro 14", "precio": 18500.00, "cantidad": 1},
        {"nombre": "Mouse inalámbrico", "precio": 420.00, "cantidad": 2},
    ]
    print(resumen_compra(carrito))
    print("Total con 10% de descuento:", calcular_total([18500.00, 840.00], 0.10))
    print("¿Hay stock?", validar_stock(5, 3))
"""

TAREA
Analiza el código y genera la documentación con esta estructura:

1. Resumen en 2 o 3 líneas: qué hace el código y para qué se usa.
2. Requisitos: dependencias, librerías o datos que necesita para funcionar.
3. Funciones o clases: para cada una indica nombre y propósito, parámetros (tipo y significado), valor de retorno y errores que puede lanzar.
4. Ejemplo de uso realista y ejecutable.
5. Casos límite o comportamientos que conviene vigilar.
6. Posibles mejoras (máximo 3, solo si son relevantes).

REGLAS
- Escribe en español claro y directo.
- No inventes funciones, parámetros ni comportamientos que no estén en el código.
- Si algo no se puede deducir del código, indícalo como "no es posible determinarlo".
- Usa formato Markdown y bloques de código cuando corresponda.
- No repitas el código completo en la respuesta; solo las partes necesarias.
```
