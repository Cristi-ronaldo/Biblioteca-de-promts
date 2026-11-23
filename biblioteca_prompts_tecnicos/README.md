# 🧰 Biblioteca de prompts técnicos

Colección de **prompts reutilizables** para pedirle a un asistente de IA tareas técnicas del día a día con siempre el mismo orden y calidad: documentar código, redactar correos técnicos y analizar incidencias. Incluye un **prompt maestro** para crear prompts nuevos, un **catálogo visual en HTML** y un **simulador en Python** que arma el prompt completo haciéndote preguntas.

**Stack:** Python 3 (solo librería estándar, sin instalar nada) · HTML/CSS/JavaScript · Markdown · JSON

---

## 📑 Contenido

1. [Prompts incluidos](#-prompts-incluidos)
2. [Inicio rápido](#-inicio-rápido)
3. [Catálogo en HTML](#-catálogo-en-html)
4. [El simulador](#️-el-simulador)
5. [Cómo funcionan las plantillas](#-cómo-funcionan-las-plantillas)
6. [Agregar un prompt nuevo](#-agregar-un-prompt-nuevo)
7. [Cómo escribir mejores prompts](#-cómo-escribir-mejores-prompts)
8. [Estructura del proyecto](#-estructura-del-proyecto)
9. [Aviso importante](#️-aviso-importante)
10. [Autor y licencia](#-autor-y-licencia)

---

## 📚 Prompts incluidos

| Prompt | Archivo | Para qué sirve |
| --- | --- | --- |
| **Documentar código** | `prompts/01_documentar_codigo.md` | Convierte un archivo de código en documentación clara: qué hace, para qué sirve y cómo se usa. |
| **Redactar correo técnico** | `prompts/02_correo_tecnico.md` | Escribe mensajes profesionales sobre mantenimientos, avances, problemas o solicitudes. |
| **Analizar incidencias** | `prompts/03_analisis_incidencias.md` | Ordena el análisis de una falla: impacto, hipótesis, mitigación y prevención. |
| **Prompt maestro** | `prompts/04_prompt_maestro.md` | Molde base para crear prompts nuevos (rol, contexto, tarea, formato, reglas y ejemplo). |

Cada archivo de prompt tiene la misma estructura: *¿Para qué sirve?*, *Cuándo usarlo*, *Cómo usarlo*, el *Prompt* listo para copiar, un *Ejemplo de resultado esperado* y *Consejos*.

---

## 🚀 Inicio rápido

**Requisitos:** Python 3. No hay dependencias que instalar.

```bash
# 1. Clonar el repositorio
git clone https://github.com/Cristi-ronaldo/biblioteca-prompts-tecnicos.git
cd biblioteca-prompts-tecnicos

# 2. Abrir el simulador
python simulador_prompts.py
```

Para ver rápido cómo funciona, elige la opción **5** del menú: genera los tres prompts con datos de ejemplo, sin hacerte preguntas, y los guarda en `salidas/`.

---

## 🌐 Catálogo en HTML

Abre `catalogo.html` directamente en tu navegador (doble clic). Muestra los cuatro prompts con un botón **Copiar** para llevarlos al portapapeles con un clic. No necesita servidor ni conexión.

---

## 🕹️ El simulador

`simulador_prompts.py` te hace preguntas sencillas y arma el prompt completo, listo para pegar en tu asistente de IA.

| Opción | Acción |
| --- | --- |
| 1 | Documentar código: pide lenguaje, público y la ruta del archivo (con Enter usa `ejemplos/codigo_ejemplo.py`). |
| 2 | Redactar correo técnico: pide destinatario, objetivo, tono, nivel técnico, puntos clave y acción esperada. |
| 3 | Analizar incidencia: pide sistema, síntoma, inicio, frecuencia, impacto, cambios recientes y logs. |
| 4 | Ver la biblioteca completa: lista los prompts con su descripción. |
| 5 | Demostración automática: genera los tres prompts con datos de ejemplo. |
| 0 | Salir. |

Cada pregunta muestra un valor de ejemplo entre corchetes; si pulsas Enter sin escribir nada, se usa ese ejemplo. Los prompts generados se guardan como `salidas/prompt_<nombre>_AAAA-MM-DD_HHMMSS.md`.

### Uso en el día a día

1. Elige la tarea que necesitas.
2. Responde las preguntas del simulador.
3. Copia el prompt que aparece en pantalla.
4. Pégalo en tu asistente de IA.
5. Revisa la respuesta y ajústala si hace falta.

---

## ⚙️ Cómo funcionan las plantillas

Los textos que usa el simulador están en `plantillas/plantillas.json`. Cada plantilla tiene un nombre, una descripción, una lista de preguntas y el texto del prompt con marcadores `{{clave}}` que se reemplazan por las respuestas:

```json
"mi_prompt": {
  "nombre": "Mi prompt",
  "descripcion": "Qué hace, en una línea.",
  "preguntas": [
    { "clave": "tema", "pregunta": "¿Sobre qué tema?", "ejemplo": "migración de base de datos" }
  ],
  "plantilla": "Actúa como un ingeniero senior.\n\nTema: {{tema}}"
}
```

Dos claves tienen un tratamiento especial:

- **`codigo`:** se interpreta como la ruta de un archivo, cuyo contenido se inserta en el prompt (junto con `{{archivo}}`, el nombre del archivo).
- **`puntos`:** los elementos separados por punto y coma (`a; b; c`) se convierten en una lista numerada.

---

## ➕ Agregar un prompt nuevo

1. **Crea el archivo** en `prompts/` (por ejemplo, `05_mi_prompt.md`) con las secciones habituales. Usa el prompt maestro como molde. La opción 4 del simulador toma la descripción de la sección `## ¿Para qué sirve?`.
2. **Agrega la plantilla** en `plantillas/plantillas.json` siguiendo el formato anterior.
3. **Agrega la opción al menú** en `simulador_prompts.py`: una línea en `main()` que llame a `ejecutar_flujo("mi_prompt", plantillas)` y, si quieres que aparezca en la demostración, su clave en la lista de `modo_demo`.
4. **(Opcional)** Añádelo a `catalogo.html`.

---

## ✍️ Cómo escribir mejores prompts

Todo prompt técnico debería responder seis preguntas (es la estructura del prompt maestro):

1. **Rol:** ¿quién debe ser la IA?
2. **Contexto:** ¿qué información necesita?
3. **Tarea:** ¿qué debe hacer exactamente?
4. **Formato:** ¿cómo quiero la respuesta?
5. **Reglas:** ¿qué debe evitar y qué límites tiene?
6. **Ejemplo:** ¿cómo se ve una buena respuesta? (opcional, pero muy útil)

Además: sé específico, da contexto, define el formato, pon límites ("no inventes datos") e itera sobre el prompt en lugar de empezar de cero.

---

## 📁 Estructura del proyecto

```text
biblioteca-prompts-tecnicos/
├── simulador_prompts.py        # Simulador de consola que arma los prompts
├── catalogo.html               # Catálogo visual con botón de copiar
├── prompts/
│   ├── 01_documentar_codigo.md
│   ├── 02_correo_tecnico.md
│   ├── 03_analisis_incidencias.md
│   └── 04_prompt_maestro.md
├── plantillas/
│   └── plantillas.json         # Textos y preguntas que usa el simulador
├── ejemplos/
│   ├── codigo_ejemplo.py       # Código de muestra para probar "Documentar código"
│   └── respuesta_ejemplo_documentacion.md   # Cómo se ve una buena respuesta
└── salidas/                    # Prompts generados (se crea al ejecutar)
```

---

## ⚠️ Aviso importante

Los prompts son textos de apoyo. Las respuestas de la IA **siempre deben revisarse** antes de enviarse a un cliente o de tomar una decisión: la responsabilidad final es de quien las usa. No pegues en un asistente de IA contraseñas, claves ni datos confidenciales de clientes o empresas.

---

## 👤 Autor y licencia

**Autor:** Cristian Lozano · GitHub: [@Cristi-ronaldo](https://github.com/Cristi-ronaldo)

**Licencia:** [MIT](LICENSE).
