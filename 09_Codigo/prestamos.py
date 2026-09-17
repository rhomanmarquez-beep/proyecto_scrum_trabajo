from datetime import datetime
from archivos import cargar_json, guardar_json

VERDE = "\033[32m"
ROJO = "\033[31m"
RESET = "\033[0m"


RUTA_EQUIPOS = "datos/equipos.json"
RUTA_ESTUDIANTES = "datos/estudiantes.json"
RUTA_PRESTAMOS = "datos/prestamos.json"

def registrar_prestamo():
    print("\n--- REGISTRAR PRÉSTAMO ---")
    
    documento = input("Documento del estudiante: ").strip()
    estudiantes = cargar_json(RUTA_ESTUDIANTES)
    estudiante = next((e for e in estudiantes if e["documento"] == documento), None)

    if not estudiante:
        print(f"{ROJO} Error: El estudiante no está registrado.{RESET}")
        return

    codigo_eq = input("Código del equipo a prestar: ").strip().upper()
    equipos = cargar_json(RUTA_EQUIPOS)
    equipo = next((eq for eq in equipos if eq["codigo"] == codigo_eq), None)

    if not equipo:
        print(f"{ROJO} Error: El equipo no fue encontrado.{RESET}")
        return

    if equipo["estado"] != "Disponible":
        print(f"{ROJO} Error: El equipo no está disponible (Estado actual: {equipo['estado']}).{RESET}")
        return

    
    equipo["estado"] = "Prestado"
    guardar_json(RUTA_EQUIPOS, equipos)

    
    prestamos = cargar_json(RUTA_PRESTAMOS)
    id_prestamo = f"PR-{len(prestamos) + 1:03d}"
    fecha_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nuevo_prestamo = {
        "id_prestamo": id_prestamo,
        "documento_estudiante": estudiante["documento"],
        "nombre_estudiante": estudiante["nombre"],
        "codigo_equipo": equipo["codigo"],
        "tipo_equipo": equipo["tipo"],
        "fecha_prestamo": fecha_inicio,
        "fecha_devolucion": None,
        "estado": "Activo"
    }

    prestamos.append(nuevo_prestamo)
    if guardar_json(RUTA_PRESTAMOS, prestamos):
        print(f"{VERDE} Préstamo registrado con éxito. ID Préstamo: {id_prestamo}{RESET}")

def registrar_devolucion():
    """HU05: Registrar devolución de equipo"""
    print("\n--- REGISTRAR DEVOLUCIÓN ---")
    codigo_eq = input("Código del equipo a devolver: ").strip().upper()

    equipos = cargar_json(RUTA_EQUIPOS)
    equipo = next((eq for eq in equipos if eq["codigo"] == codigo_eq), None)

    if not equipo:
        print(f"{ROJO} Error: El equipo no fue encontrado.{RESET}")
        return

    if equipo["estado"] != "Prestado":
        print(f"{ROJO} Error: El equipo no figura como prestado.{RESET}")
        return

    prestamos = cargar_json(RUTA_PRESTAMOS)
    prestamo_activo = next((p for p in prestamos if p["codigo_equipo"] == codigo_eq and p["estado"] == "Activo"), None)

    if not prestamo_activo:
        print(f"{ROJO} Error: No se encontró un registro de préstamo activo para este equipo.{RESET}")
        return


    prestamo_activo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prestamo_activo["estado"] = "Finalizado"
    guardar_json(RUTA_PRESTAMOS, prestamos)


    equipo["estado"] = "Disponible"
    guardar_json(RUTA_EQUIPOS, equipos)

    print(f"{VERDE} Devolución del equipo {codigo_eq} completada y registrada exitosamente.{RESET}")

def consultar_prestamos_activos():
    print("\n--- EQUIPOS ACTUALMENTE PRESTADOS ---")
    prestamos = cargar_json(RUTA_PRESTAMOS)
    activos = [p for p in prestamos if p["estado"] == "Activo"]

    if not activos:
        print("No hay préstamos activos en este momento.")
        return

    print(f"{'ID Préstamo':<12} | {'Equipo':<10} | {'Tipo':<12} | {'Estudiante':<20} | {'Fecha Préstamo':<20}")
    print("-" * 80)
    for p in activos:
        print(f"{p['id_prestamo']:<12} | {p['codigo_equipo']:<10} | {p['tipo_equipo']:<12} | {p['nombre_estudiante']:<20} | {p['fecha_prestamo']:<20}")

def consultar_historial_prestamos():
    print("\n--- HISTORIAL COMPLETO DE PRÉSTAMOS ---")
    prestamos = cargar_json(RUTA_PRESTAMOS)

    if not prestamos:
        print("No hay registros en el historial de préstamos.")
        return

    print(f"{'ID':<8} | {'Equipo':<8} | {'Estudiante':<18} | {'Estado':<10} | {'Fecha Préstamo':<19} | {'Fecha Devolución'}")
    print("-" * 85)
    for p in prestamos:
        dev = p['fecha_devolucion'] if p['fecha_devolucion'] else 'Pendiente'
        print(f"{p['id_prestamo']:<8} | {p['codigo_equipo']:<8} | {p['nombre_estudiante']:<18} | {p['estado']:<10} | {p['fecha_prestamo']:<19} | {dev}")