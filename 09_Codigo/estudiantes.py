from archivos import cargar_json, guardar_json
VERDE = "\033[32m"
ROJO = "\033[31m"
RESET = "\033[0m"


RUTA_ESTUDIANTES = "datos/estudiantes.json"

def registrar_estudiante():
    print("\n--- REGISTRAR NUEVO ESTUDIANTE ---")
    documento = input("Documento de identidad: ").strip()

    estudiantes = cargar_json(RUTA_ESTUDIANTES)
    for est in estudiantes:
        if est["documento"] == documento:
            print(f"{ROJO} Error: Ya existe un estudiante registrado con ese documento.{RESET}")
            return

    nombre = input("Nombre completo: ").strip().title()
    correo = input("Correo institucional: ").strip().lower()
    programa = input("Programa académico: ").strip().title()

    if not documento or not nombre or not correo:
        print(f"{ROJO} Error: Todos los campos son obligatorios.{RESET}")
        return

    nuevo_estudiante = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa": programa
    }

    estudiantes.append(nuevo_estudiante)
    if guardar_json(RUTA_ESTUDIANTES, estudiantes):
        print(f"{VERDE} Estudiante {nombre} registrado con éxito.{RESET}")

def listar_estudiantes():
    print("\n--- LISTA DE ESTUDIANTES ---")
    estudiantes = cargar_json(RUTA_ESTUDIANTES)
    if not estudiantes:
        print(f"{ROJO}No hay estudiantes registrados.{RESET}")
        return

    print(f"{'Documento':<12} | {'Nombre':<22} | {'Correo':<25} | {'Programa':<15}")
    print("-" * 80)
    for est in estudiantes:
        print(f"{est['documento']:<12} | {est['nombre']:<22} | {est['correo']:<25} | {est['programa']:<15}")