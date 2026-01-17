# 🗄️ Centralized Data API (CRUD System)

Este proyecto consiste en una estructura de **backend robusta** diseñada para la gestión centralizada de bases de datos. Permite realizar las operaciones fundamentales de **CRUD** (Create, Read, Update, Delete) de forma eficiente, garantizando la integridad y seguridad de los registros en todo momento.

> [!IMPORTANT]
> **OBJETIVO:** Centralizar el flujo de información entre la base de datos y la interfaz de usuario, utilizando estándares de seguridad para prevenir la inyección de datos maliciosos.

---

## ✨ Características
- **Operaciones CRUD Completas:** Interfaz estandarizada para crear, leer, actualizar y eliminar datos.
- **Seguridad de Datos:** Implementación de consultas preparadas para evitar ataques de Inyección SQL.
- **Arquitectura Escalable:** Diseñada para crecer y soportar múltiples tablas o tipos de datos.
- **Validación de Entradas:** Filtros automáticos para asegurar que solo la información correcta sea procesada.

---

## 🛠️ Tecnologías y Conceptos

Para dominar este software, es fundamental entender los pilares del desarrollo de backend:

* **API (Application Programming Interface):** El puente que permite que diferentes programas se comuniquen con la base de datos.
* **Bases de Datos (SQL/NoSQL):** El lugar donde se almacena la información de forma estructurada.
* **CRUD:** El acrónimo de las cuatro funciones básicas que todo software de gestión debe tener.
* **Manejo de Excepciones:** Bloques de código que evitan que el programa se cierre si hay un error en la base de datos.

---

## 🚀 Instalación y Configuración del Entorno

Para mantener este proyecto limpio y profesional, es obligatorio usar un **entorno virtual (venv)**. Esto evita conflictos entre las librerías de tus diferentes proyectos de ciberseguridad.

### 1. Preparar el Entorno Virtual
Abre tu terminal en la carpeta del proyecto y ejecuta:

**En Windows:**

# Crear el entorno
python -m venv venv

# Activar el entorno
.\venv\Scripts\activate
En Linux / Mac:

Bash

# Crear el entorno
python3 -m venv venv

# Activar el entorno
source venv/bin/activate
2. Instalación de dependencias
Una vez activo el (venv), instala las librerías necesarias (ej. flask o sqlalchemy):

```bash

pip install flask sqlalchemy



---
