# Prompt generado: Analizar incidencias

Generado el 23/11/2026 a las 23:09.

Copia el texto del bloque y pégalo en tu asistente de IA.

```text
Actúa como un analista de incidencias senior (SRE / soporte técnico nivel 3).

CONTEXTO
- Sistema afectado: el portal de pagos
- Síntoma observado: responde error 500 al 30% de los usuarios
- Cuándo empezó: hoy a las 09:15
- Frecuencia: intermitente
- Impacto en el negocio: alto: los clientes no pueden completar pagos
- Cambios recientes: ninguno
- Logs o mensajes de error:
"""
sin logs disponibles
"""

TAREA
Entrega un análisis con este orden:

1. Resumen ejecutivo en 3 líneas, entendible para alguien no técnico.
2. Impacto: a quién afecta, desde cuándo y qué se pierde mientras no se resuelve.
3. Hipótesis ordenadas de mayor a menor probabilidad, con el motivo de cada una.
4. Para cada hipótesis: cómo confirmarla o descartarla (comandos, consultas, revisión de configuración o preguntas al equipo).
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
