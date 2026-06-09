# 🗓️ Gestor de Reservas - Django Backend
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
</p>

Este proyecto es una aplicación web robusta construida con **Django** para gestionar la reserva de recursos (canchas, salas, equipos, etc.). Incluye validaciones inteligentes y un diseño moderno en modo oscuro.

## ✨ Características Principales
- **Gestión de Recursos**: Visualización dinámica de disponibilidad.
- **Validación Anti-Solapamiento**: El sistema impide reservas en horarios que ya están ocupados en la base de datos de manera atómica.
- **Reservas Recurrentes**: Funcionalidad para repetir una reserva semanalmente durante un mes (4 semanas) de manera automática.
- **Sistema de Notificaciones**: Feedback visual interactivo en caso de éxito y errores.
- **Seguridad**: Autenticación de usuarios y protección de rutas con Django Auth.
- **Interfaz Dark Mode**: Diseño limpio, enfocado y profesional utilizando CSS independiente y responsivo.

## 🛠️ Instalación y Configuración Local
1. Clona el repositorio: `git clone https://github.com/federicovolpintesta-eng/GESTOR_RESERVAS.git`
2. Crea un entorno virtual: `python -m venv venv`
3. Activa tu entorno e instala las dependencias: `pip install -r requirements.txt`
4. Aplica las migraciones: `python manage.py migrate`
5. Levanta el servidor: `python manage.py runserver`
