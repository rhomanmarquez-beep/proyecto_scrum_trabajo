import os
from equipos import registrar_equipo, listar_equipos, eliminar_equipo
from estudiantes import registrar_estudiante, listar_estudiantes
from prestamos import (
    registrar_prestamo,
    registrar_devolucion,
    consultar_prestamos_activos,
    consultar_historial_prestamos
)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

AZUL = "\033[34m"
VERDE = "\033[32m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
CELESTE = "\033[36m"
MORADO = "\033[35m"
RESET = "\033[0m"

def inicializar_archivos():
    os.makedirs("datos", exist_ok=True)

def mostrar_menu():
    print("\n" + "="*50)
    print(" SISTEMA DE PRÉSTAMO DE EQUIPOS TECNOLÓGICOS (MVP)")
    print("="*50)
    print(f"{AZUL}1. Administrar Equipos{RESET}")
    print(f"{AMARILLO}2. Administrar estudiantes{RESET}")
    print(f"{MORADO}3. Administrar Préstamos{RESET}")
    print(f"{ROJO}4. Salir del Programa{RESET}")
    print("="*50)

def menu_equipos():
    inicializar_archivos()
    while True:
        print("\n" + f"{AZUL}={RESET}"*40)
        print(f"{AZUL}=== ADMINISTRAR EQUIPOS ==={RESET}")
        print("\n" + f"{AZUL}={RESET}"*40)
        print(f"{AZUL}1. Registrar equipo (HU01){RESET}")
        print(f"{AZUL}2. Consultar equipos / disponibilidad (HU02) {RESET}")
        print(f"{AZUL}3. Eliminar equipo del inventario (HU08){RESET}")
        print(f"{ROJO}4. Volver al menú{RESET}")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            eliminar_equipo()
        elif opcion == "4":
            clear()
            break
        else:
            print(f"{ROJO}Opción no válida. Intente nuevamente.{RESET}")

def menu_estudiantes():
    inicializar_archivos()
    while True:
        print("\n" + f"{AMARILLO}={RESET}"*40)
        print(f"{AMARILLO} === ADMINISTRAR ESTUDIANTES === {RESET}")
        print("\n" + f"{AMARILLO}={RESET}"*40)
        print(f"{AMARILLO}1. Registrar estudiante (HU03) {RESET}")
        print(f"{AMARILLO}2. Listar estudiantes {RESET}")
        print(f"{ROJO}3. Volver al menú principal {RESET}")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            clear()
            break
        else:
            print(f"{ROJO}Opción inválida, Intente nuevamente{RESET}")

def menu_prestamos():
    inicializar_archivos()
    while True:
        print("\n" + f"{MORADO}={RESET}"*40)
        print(f"{MORADO} === ADMINISTRAR PRESTAMOS === {RESET}")
        print("\n" + f"{MORADO}={RESET}"*40)
        print(f"{MORADO}1. Registrar Préstamo de equipo (HU04){RESET}")
        print(f"{MORADO}2. Registrar devolución de equipo (HU05){RESET}")
        print(f"{MORADO}3. Consultar equipos actualmente prestadios (HU06){RESET}")
        print(f"{MORADO}4. Consultar historial de préstamos (HU07){RESET}")
        print(f"{ROJO}5. Volver al menú principal{RESET}")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            registrar_devolucion()
        elif opcion == "3":
            consultar_prestamos_activos()
        elif opcion == "4":
            consultar_historial_prestamos()
        elif opcion == "5":
            clear()
            break
        else:
            print(f"{ROJO}Opción no válida. Intente nuevamente.{RESET}")
            

def main():
    inicializar_archivos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            clear()
            menu_equipos()
        elif opcion == "2":
            clear()
            menu_estudiantes()
        elif opcion == "3":
            clear()
            menu_prestamos()
        elif opcion == "4":
            print(f"{VERDE}\n ¡Gracias por usar el sistema! Finalizando aplicación...{RESET}")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    clear()
    main()