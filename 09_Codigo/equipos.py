from archivos import cargar_json, guardar_json

AZUL = "\033[34m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
CELESTE = "\033[36m"
MORADO = "\033[35m"
RESET = "\033[0m"

RUTA_EQUIPOS = "datos/equipos.json"

def registrar_equipo():
  
    print("\n--- REGISTRAR NUEVO EQUIPO ---")
    codigo = input("Código del equipo (ej. EQ-001): ").strip().upper()
    
    equipos = cargar_json(RUTA_EQUIPOS)
    for eq in equipos:
        if eq["codigo"] == codigo:
            print(f"{ROJO} Error: Ya existe un equipo con ese código.{RESET}")
            return

    tipo = input("Tipo (ej. Laptop, Tablet, Proyector): ").strip().capitalize()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    nuevo_equipo = {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": "Disponible"
    }

    equipos.append(nuevo_equipo)
    if guardar_json(RUTA_EQUIPOS, equipos):
        print(f" Equipo {codigo} registrado con éxito.")

def listar_equipos():
    print("\n--- INVENTARIO DE EQUIPOS ---")
    equipos = cargar_json(RUTA_EQUIPOS)
    if not equipos:
        print("No hay equipos registrados en el sistema.")
        return

    print(f"{'Código':<10} | {'Tipo':<12} | {'Marca':<12} | {'Modelo':<12} | {'Estado':<12}")
    print("-" * 65)
    for eq in equipos:
        print(f"{eq['codigo']:<10} | {eq['tipo']:<12} | {eq['marca']:<12} | {eq['modelo']:<12} | {eq['estado']:<12}")

def eliminar_equipo():
    print(f"{ROJO}\n--- ELIMINAR EQUIPO ---{RESET}")
    codigo = input("Código del equipo a eliminar: ").strip().upper()
    
    equipos = cargar_json(RUTA_EQUIPOS)
    equipo_encontrado = None

    for eq in equipos:
        if eq["codigo"] == codigo:
            equipo_encontrado = eq
            break

    if not equipo_encontrado:
        print(f"{ROJO} Error: El equipo no fue encontrado.{RESET}")
        return

    if equipo_encontrado["estado"] == "Prestado":
        print(f"{ROJO} Error: No se puede eliminar un equipo que está actualmente prestado.{RESET}")
        return

    equipos.remove(equipo_encontrado)
    if guardar_json(RUTA_EQUIPOS, equipos):
        print(f"{VERDE} Equipo {codigo} eliminado correctamente.{RESET}")