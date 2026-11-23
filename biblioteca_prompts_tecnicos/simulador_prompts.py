"""
SIMULADOR de la "Biblioteca de prompts técnicos".

No necesitas saber programar: el simulador te hace preguntas sencillas y
arma el prompt completo, listo para copiar y pegar en tu asistente de IA.

Uso:
    python simulador_prompts.py
"""

import json
import os
from datetime import datetime

CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_PLANTILLAS = os.path.join(CARPETA, "plantillas", "plantillas.json")
CARPETA_PROMPTS = os.path.join(CARPETA, "prompts")
CARPETA_SALIDAS = os.path.join(CARPETA, "salidas")
CODIGO_EJEMPLO = os.path.join(CARPETA, "ejemplos", "codigo_ejemplo.py")


def separador():
    print("-" * 64)


def cargar_plantillas():
    with open(RUTA_PLANTILLAS, encoding="utf-8") as archivo:
        return json.load(archivo)


def preguntar(texto, ejemplo="", obligatorio=False):
    """Hace una pregunta y devuelve la respuesta (o el ejemplo si se deja vacío)."""
    pista = f" [{ejemplo}]" if ejemplo else ""
    while True:
        respuesta = input(f"  {texto}{pista}: ").strip()
        if respuesta:
            return respuesta
        if ejemplo:
            return ejemplo
        if not obligatorio:
            return ""
        print("  Este dato es necesario, intenta de nuevo.")


def formatear_puntos(texto):
    """Convierte 'a; b; c' en una lista numerada para el prompt."""
    partes = [p.strip() for p in texto.split(";") if p.strip()]
    return "\n".join(f"  {i}. {parte}" for i, parte in enumerate(partes, start=1))


def leer_codigo(ruta):
    """Lee el archivo de código indicado. Si no existe, usa el de ejemplo."""
    if not ruta:
        ruta = CODIGO_EJEMPLO
    if not os.path.isabs(ruta):
        ruta = os.path.join(CARPETA, ruta)
    if not os.path.exists(ruta):
        print(f"  No se encontró el archivo, se usará el ejemplo incluido.")
        ruta = CODIGO_EJEMPLO
    with open(ruta, encoding="utf-8") as archivo:
        return archivo.read().strip(), os.path.basename(ruta)


def construir_prompt(plantilla, respuestas):
    """Reemplaza los marcadores {{clave}} por las respuestas."""
    texto = plantilla["plantilla"]
    for clave, valor in respuestas.items():
        texto = texto.replace("{{" + clave + "}}", str(valor))
    return texto


def guardar_prompt(clave, nombre, texto):
    os.makedirs(CARPETA_SALIDAS, exist_ok=True)
    archivo = f"prompt_{clave}_{datetime.now():%Y-%m-%d_%H%M%S}.md"
    ruta = os.path.join(CARPETA_SALIDAS, archivo)
    contenido = (
        f"# Prompt generado: {nombre}\n\n"
        f"Generado el {datetime.now():%d/%m/%Y a las %H:%M}.\n\n"
        "Copia el texto del bloque y pégalo en tu asistente de IA.\n\n"
        "```text\n" + texto + "\n```\n"
    )
    with open(ruta, "w", encoding="utf-8") as destino:
        destino.write(contenido)
    return ruta


def ejecutar_flujo(clave, plantillas, modo_demo=False):
    """Pregunta los datos, arma el prompt y lo guarda."""
    plantilla = plantillas[clave]
    print(f"\n=== {plantilla['nombre'].upper()} ===")
    print(plantilla["descripcion"])
    separador()

    respuestas = {}
    for dato in plantilla["preguntas"]:
        clave_dato = dato["clave"]
        if modo_demo:
            valor = dato["ejemplo"]
        else:
            valor = preguntar(dato["pregunta"], dato["ejemplo"])

        if clave_dato == "codigo":
            codigo, nombre_archivo = leer_codigo(valor)
            respuestas["codigo"] = codigo
            respuestas["archivo"] = nombre_archivo
        elif clave_dato == "puntos":
            respuestas["puntos"] = formatear_puntos(valor)
        else:
            respuestas[clave_dato] = valor

    texto = construir_prompt(plantilla, respuestas)
    ruta = guardar_prompt(clave, plantilla["nombre"], texto)

    separador()
    print("PROMPT LISTO:\n")
    print(texto)
    separador()
    print(f"Guardado en: {ruta}")
    print("Copia ese texto y pégalo en tu asistente de IA.")
    return ruta


def ver_biblioteca():
    print("\nBIBLIOTECA DE PROMPTS")
    separador()
    archivos = sorted(f for f in os.listdir(CARPETA_PROMPTS) if f.endswith(".md"))
    for archivo in archivos:
        ruta = os.path.join(CARPETA_PROMPTS, archivo)
        with open(ruta, encoding="utf-8") as f:
            lineas = f.read().splitlines()

        titulo = next((l.lstrip("# ").strip() for l in lineas if l.startswith("# ")), archivo)
        descripcion = ""
        for i, linea in enumerate(lineas):
            if linea.strip().startswith("## ¿Para qué sirve?"):
                partes = []
                for siguiente in lineas[i + 1:]:
                    if not siguiente.strip():
                        if partes:
                            break
                        continue
                    partes.append(siguiente.strip())
                descripcion = " ".join(partes)
                break
        print(f"  • {titulo}")
        print(f"    {descripcion}")
        print(f"    Archivo: prompts/{archivo}\n")
    separador()


def modo_demo(plantillas):
    print("\nMODO DEMOSTRACIÓN")
    print("Se generarán los tres prompts con datos de ejemplo, sin preguntar nada.")
    rutas = []
    for clave in ("documentar_codigo", "correo_tecnico", "analisis_incidencias"):
        rutas.append(ejecutar_flujo(clave, plantillas, modo_demo=True))
    print("\nDemostración terminada. Se generaron estos archivos:")
    for ruta in rutas:
        print(f"  - {ruta}")


def main():
    plantillas = cargar_plantillas()

    while True:
        print()
        print("=" * 64)
        print("   BIBLIOTECA DE PROMPTS TÉCNICOS")
        print("=" * 64)
        print("  1. Documentar código")
        print("  2. Redactar un correo técnico")
        print("  3. Analizar una incidencia")
        print("  4. Ver la biblioteca completa")
        print("  5. Demostración automática (los 3 prompts)")
        print("  0. Salir")
        print("=" * 64)
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ejecutar_flujo("documentar_codigo", plantillas)
        elif opcion == "2":
            ejecutar_flujo("correo_tecnico", plantillas)
        elif opcion == "3":
            ejecutar_flujo("analisis_incidencias", plantillas)
        elif opcion == "4":
            ver_biblioteca()
        elif opcion == "5":
            modo_demo(plantillas)
        elif opcion == "0":
            print("\nHasta luego. Tus prompts quedan guardados en la carpeta salidas/.")
            break
        else:
            print("\nOpción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
