# Sistema de Gestión de Reservas - Django 🚀

Este proyecto es una aplicación web robusta construida con **Django** para gestionar la reserva de recursos (canchas, salas, equipos, etc.). Incluye validaciones inteligentes y un diseño moderno en modo oscuro.

## ✨ Características Principales
- **Gestión de Recursos**: Visualización dinámica de disponibilidad.
- **Validación Anti-Solapamiento**: El sistema impide reservas en horarios que ya están ocupados.
- **Reservas Recurrentes**: Funcionalidad para repetir una reserva semanalmente durante un mes (4 semanas) con un solo clic.
- **Sistema de Notificaciones**: Mensajes visuales de éxito y error según el resultado de la operación.
- **Seguridad**: Autenticación de usuarios y protección de rutas.
- **Interfaz Dark Mode**: Diseño limpio y profesional utilizando CSS independiente.

## 🛠️ Instalación y Configuración Local
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`.
3. Activar el entorno virtual.
4. Instalar dependencias: `pip install -r requirements.txt`.
5. Ejecutar migraciones: `python manage.py migrate`.
6. Iniciar servidor: `python manage.py runserver`.

## 🧑‍💻 Información para el Evaluador
El sistema cuenta con un panel de administración en `/admin`. 
Las credenciales de acceso se detallan en el formulario de entrega.
