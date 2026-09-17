import json
import os

def cargar_json(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        return []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def guardar_json(ruta_archivo, datos):
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"Error al guardar los datos: {e}")
        return False