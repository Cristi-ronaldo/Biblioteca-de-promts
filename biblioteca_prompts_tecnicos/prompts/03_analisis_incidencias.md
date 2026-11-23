# Prompt: Analizar incidencias

## ¿Para qué sirve?

Ordena el análisis de un problema técnico: qué está pasando, cuál es el
impacto, qué hipótesis existen, cómo confirmarlas y qué hacer para resolverlo
y para que no vuelva a ocurrir.

## Cuándo usarlo

- Cuando hay una caída o un error que no sabes por dónde empezar.
- Para preparar el reporte de una incidencia (post-mortem).
- Para priorizar hipótesis antes de tocar el sistema.
- Para explicar a gerencia qué pasó, sin tecnicismos.

## Cómo usarlo

1. Copia el prompt.
2. Describe el síntoma con el mayor detalle posible (mensajes de error,
   horarios, frecuencia, a quién afecta).
3. Pega los logs o mensajes relevantes.
4. Si no tienes logs, escribe "sin logs disponibles".

---

## Prompt

```text
Actúa como un analista de incidencias senior (SRE / soporte técnico nivel 3).

CONTEXTO
- Sistema afectado: [NOMBRE DEL SISTEMA O SERVICIO]
- Síntoma observado: [QUÉ ESTÁ FALLANDO, CON EL MAYOR DETALLE POSIBLE]
- Cuándo empezó: [FECHA Y HORA APROXIMADA]
- Frecuencia: [SIEMPRE / INTERMITENTE / UNA SOLA VEZ]
- Usuarios o procesos afectados: [QUIÉNES Y CUÁNTOS]
- Impacto en el negocio: [ALTO / MEDIO / BAJO, Y POR QUÉ]
- Cambios recientes: [DEPLOY, ACTUALIZACIÓN, CAMBIO DE CONFIGURACIÓN O "NINGUNO"]
- Logs o mensajes de error:
"""
[PEGA AQUÍ LOS LOGS]
"""

TAREA
Entrega un análisis con este orden:

1. Resumen ejecutivo en 3 líneas, entendible para alguien no técnico.
2. Impacto: a quién afecta, desde cuándo y qué se pierde mientras no se resuelve.
3. Hipótesis ordenadas de mayor a menor probabilidad, con el motivo de cada una.
4. Para cada hipótesis: cómo confirmarla o descartarla (comandos, consultas,
   revisión de configuración o preguntas al equipo).
5. Mitigación inmediata: qué hacer ahora para reducir el impacto.
6. Solución definitiva probable y qué se necesita para aplicarla.
7. Prevención: 3 acciones concretas para evitar que se repita.
8. Información que falta y que conviene pedir.

REGLAS
- No afirmes una causa como segura si no está confirmada por los datos.
- Separa claramente "hecho observado" de "hipótesis".
- Si los logs no alcanzan, dilo y explica qué evidencia hace falta.
- Usa español claro; explica cualquier término técnico que aparezca.
- Prioriza siempre reducir el impacto antes de buscar la causa raíz.
```

## Ejemplo de resultado esperado

> **Resumen:** Desde las 09:15 el portal de pagos responde con error 500 a
> aproximadamente el 30% de los usuarios. El resto del sitio funciona normal.
>
> **Impacto:** Los clientes no pueden completar pagos. Se estima una pérdida
> de 40 transacciones por hora.
>
> **Hipótesis 1 (alta):** El servicio de pagos perdió conexión con el banco.
> **Cómo confirmar:** revisar el log `payment-gateway.log` y probar la conexión
> al endpoint del proveedor.

## Consejos

- Mientras más detallado sea el síntoma, mejor será el análisis.
- Pide que repita el análisis cuando tengas nueva evidencia.
- Guarda el resultado: es la base del reporte post-incidente.
