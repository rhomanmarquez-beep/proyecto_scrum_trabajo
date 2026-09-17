#  Sistema de Préstamo de Equipos Tecnológicos (MVP)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-Scrum-green)
![Estado](https://img.shields.io/badge/Estado-Finalizado-brightgreen)

Sistema de consola desarrollado en **Python** bajo el marco de trabajo ágil **Scrum**, diseñado para automatizar el control de inventario, registro de estudiantes y la gestión de préstamos y devoluciones de recursos tecnológicos en instituciones educativas.

---

##  Tabla de Contenidos
- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Características Principales](#-características-principales)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación y Ejecución](#-instalación-y-ejecución)
- [Historial de Versiones](#-historial-de-versiones)
- [Equipo de Desarrollo](#-equipo-de-desarrollo)

---

## 🚀 Descripción del Proyecto

Este Producto Mínimo Viable (MVP) resuelve la problemática de la gestión manual del inventario de equipos tecnológicos. A través de una interfaz interactiva por consola con códigos de colores ANSI, permite registrar usuarios, gestionar el catálogo de equipos, realizar préstamos en tiempo real con actualización automática de estado y guardar un historial completo de operaciones persistido en archivos JSON.

---

##  Características Principales

El sistema cubre 8 Historias de Usuario (HU01 a HU08) organizadas en 3 Épicas:

* **Gestión de Inventario (HU01, HU02, HU08):**
  * Registro de equipos con código único y asignación automática del estado `"Disponible"`.
  * Consulta general de equipos y disponibilidad en formato de tabla.
  * Eliminación de equipos garantizando que no tengan préstamos activos.
* **Gestión de Estudiantes (HU03):**
  * Registro de estudiantes con validación de documento de identidad único y correo institucional.
  * Consulta del listado de alumnos registrados.
* **Control de Préstamos y Devoluciones (HU04, HU05, HU06, HU07):**
  * Asignación de préstamos validando disponibilidad del equipo y registro del estudiante.
  * Devolución de equipos con actualización automática a `"Disponible"` y registro de fecha/hora.
  * Consulta de préstamos activos e historial general de transacciones.

---

##  Arquitectura del Proyecto

El proyecto está diseñado bajo una arquitectura modular y limpia, separando las responsabilidades de cada entidad y la capa de persistencia:

```text
.
├── main.py             # Punto de entrada principal y menú interactivo por colores
├── equipos.py          # Lógica de negocio del inventario (HU01, HU02, HU08)
├── estudiantes.py      # Lógica de negocio de usuarios/estudiantes (HU03)
├── prestamos.py        # Lógica de préstamos, devoluciones e historial (HU04 - HU07)
├── archivos.py         # Módulo de lectura y escritura en formato JSON
├── datos/              # Directorio de persistencia de datos
│   ├── equipos.json
│   ├── estudiantes.json
│   └── prestamos.json
└── README.md           # Guía e instrucciones del proyecto
