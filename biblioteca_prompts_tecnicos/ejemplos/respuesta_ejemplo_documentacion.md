# Ejemplo de respuesta generada con el prompt "Documentar código"

Este es el tipo de respuesta que se obtiene al usar el prompt con el archivo
`ejemplos/codigo_ejemplo.py`. Sirve para que veas el resultado antes de usarlo.

---

## 1. Resumen

El módulo contiene tres funciones de apoyo para una tienda: calcular el total
de una compra con descuento, validar si hay stock suficiente y generar un
resumen legible de un carrito. Se usa antes de confirmar una venta.

## 2. Requisitos

- Python 3.6 o superior.
- No requiere librerías externas.
- Recibe listas y diccionarios con una estructura específica (ver abajo).

## 3. Funciones

### `calcular_total(precios, descuento=0.0)`
- **Propósito:** sumar una lista de precios y aplicar un descuento.
- **Parámetros:**
  - `precios` (lista de números): precios unitarios o subtotales.
  - `descuento` (número entre 0 y 1): 0.10 equivale a 10%.
- **Devuelve:** número redondeado a 2 decimales.
- **Errores:** `ValueError` si la lista está vacía o el descuento está fuera de rango.

### `validar_stock(stock_disponible, cantidad_solicitada)`
- **Propósito:** comprobar si hay unidades suficientes.
- **Parámetros:** ambos enteros.
- **Devuelve:** `True` o `False`.
- **Errores:** `ValueError` si la cantidad solicitada es cero o negativa.

### `resumen_compra(productos)`
- **Propósito:** armar un texto con el detalle y el total de la compra.
- **Parámetros:** lista de diccionarios con `nombre`, `precio` y `cantidad`.
- **Devuelve:** texto multilínea. Si la lista está vacía, devuelve un mensaje.
- **Errores:** `KeyError` si a un producto le falta alguna de las tres claves.

## 4. Ejemplo de uso

```python
carrito = [
    {"nombre": "Laptop Pro 14", "precio": 18500.00, "cantidad": 1},
    {"nombre": "Mouse inalámbrico", "precio": 420.00, "cantidad": 2},
]

print(resumen_compra(carrito))
print(calcular_total([18500.00, 840.00], 0.10))
print(validar_stock(5, 3))
```

## 5. Casos límite a vigilar

- `calcular_total` no valida que los precios sean números positivos.
- `resumen_compra` no aplica descuentos ni impuestos: solo suma.
- El total de `resumen_compra` no se redondea, a diferencia de `calcular_total`.
- Los precios se muestran con formato de moneda, pero la moneda no se especifica.

## 6. Posibles mejoras

1. Validar que los precios sean números mayores o iguales a cero.
2. Unificar el redondeo entre `calcular_total` y `resumen_compra`.
3. Recibir la moneda como parámetro para no asumir pesos.
