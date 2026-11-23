# Prompt: Documentar código

## ¿Para qué sirve?

Convierte un bloque de código (o un archivo completo) en documentación clara:
qué hace, qué recibe, qué devuelve y qué casos especiales contempla. Sirve para
que otra persona pueda entender y usar el código sin tener que adivinar.

## Cuándo usarlo

- Cuando heredas código de otra persona o de otro equipo.
- Antes de entregar un proyecto a un cliente.
- Cuando vas a modificar una función y necesitas entenderla primero.
- Para generar la documentación técnica de una API o una librería interna.

## Cómo usarlo

1. Copia el prompt completo.
2. Pega el código donde dice `[PEGA AQUÍ EL CÓDIGO]`.
3. Ajusta el lenguaje, el público y el formato si lo necesitas.
4. Envía el prompt a tu asistente de IA.

---

## Prompt

```text
Actúa como un ingeniero de software senior especializado en documentación técnica.

CONTEXTO
Tengo el siguiente código escrito en [LENGUAJE]. Necesito documentarlo para
que lo entienda [PÚBLICO: por ejemplo, un compañero nuevo del equipo / un
cliente sin perfil técnico / otro desarrollador que dará mantenimiento].

CÓDIGO
"""
[PEGA AQUÍ EL CÓDIGO]
"""

TAREA
Analiza el código y genera la documentación con esta estructura:

1. Resumen en 2 o 3 líneas: qué hace el código y para qué se usa.
2. Requisitos: dependencias, librerías o datos que necesita para funcionar.
3. Funciones o clases: para cada una indica
   - nombre y propósito,
   - parámetros (tipo y significado),
   - valor de retorno,
   - errores o excepciones que puede lanzar.
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

## Ejemplo de resultado esperado

> **Resumen:** La función `calcular_total` recibe una lista de precios y un
> porcentaje de descuento, y devuelve el total a pagar ya con el descuento
> aplicado. Se usa en el cierre de cada venta.
>
> **Parámetros:** `precios` (lista de números), `descuento` (número entre 0 y 1).
> **Devuelve:** número con el total final.
> **Errores:** lanza `ValueError` si el descuento está fuera de rango.

## Consejos

- Si el código es muy largo, divídelo por módulos y documenta uno a la vez.
- Pide primero un resumen y después el detalle: así detectas rápido si la IA
  entendió bien el propósito.
- Guarda la respuesta junto al código, en un archivo `DOCUMENTACION.md`.
