# Prompt maestro: estructura reutilizable

## ¿Para qué sirve?

Es una plantilla base para crear cualquier prompt técnico nuevo. En lugar de
improvisar, se llena esta estructura y el resultado suele ser mucho más claro
y útil. Sirve como "molde" para los otros prompts de la biblioteca.

## La estructura de un buen prompt

Todo prompt técnico debería responder estas seis preguntas:

1. **Rol**: ¿quién debe ser la IA? (ingeniero senior, analista, redactor...)
2. **Contexto**: ¿qué información necesita para responder bien?
3. **Tarea**: ¿qué debe hacer exactamente?
4. **Formato**: ¿cómo quiero la respuesta? (tabla, lista, correo, código...)
5. **Reglas**: ¿qué debe evitar? ¿qué límites tiene?
6. **Ejemplo**: ¿cómo se ve una buena respuesta? (opcional pero muy útil)

---

## Prompt

```text
Actúa como [ROL ESPECÍFICO CON EXPERIENCIA].

CONTEXTO
[EXPLICA LA SITUACIÓN: qué tienes, para qué lo necesitas, quién lo va a leer
y qué restricciones existen. Incluye aquí los datos de entrada.]

TAREA
[DESCRIBE LA TAREA EN PASOS CONCRETOS Y NUMERADOS.]

FORMATO DE SALIDA
[INDICA LA ESTRUCTURA EXACTA: secciones, tablas, longitud máxima, idioma.]

REGLAS
- [REGLA 1: por ejemplo, no inventar datos]
- [REGLA 2: por ejemplo, español claro, sin tecnicismos innecesarios]
- [REGLA 3: por ejemplo, si falta información, preguntar antes de responder]

EJEMPLO DE BUENA RESPUESTA (OPCIONAL)
"""
[PEGA UN EJEMPLO CORTO DEL RESULTADO QUE ESPERAS]
"""
```

## Ejemplo lleno

```text
Actúa como un ingeniero de datos con 10 años de experiencia.

CONTEXTO
Tengo una tabla de ventas con columnas fecha, sucursal, producto y monto.
Necesito explicar a gerencia cómo se comportaron las ventas del último
trimestre. La audiencia no tiene perfil técnico.

TAREA
1. Identifica las tres tendencias más importantes.
2. Explica cada una en dos frases.
3. Señala un riesgo y una recomendación.

FORMATO DE SALIDA
Un párrafo de resumen y luego tres secciones con título. Máximo 300 palabras.

REGLAS
- No uses siglas sin explicarlas.
- No inventes cifras: usa solo los datos que te doy.
- Si falta información, pregunta antes de responder.
```

## Consejos

- Un prompt específico vale más que diez prompts vagos.
- Si la respuesta no sirve, no empieces de cero: corrige el contexto o el formato.
- Guarda los prompts que te funcionen; con el tiempo forman tu propia biblioteca.
