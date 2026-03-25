# Asistencia de IA

Este documento registra el proceso de asistencia de herramientas de IA durante el desarrollo del proyecto Temporizador Pomodoro.

## Sesiones de Asistencia

### Sesión 1: Generación Inicial del Código
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Generación del README.md
  - Configuración de .gitignore
  - Creación de requirements.txt
  - Desarrollo de módulos: config.py, notificaciones.py, pomodoro.py
- Modificaciones realizadas: Agregados comentarios explicativos en el código.

### Sesión 2: Fase 4 - Configuración Personalizable
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Modificación de config.py para incluir configuración interactiva con validación de valores positivos.
  - Actualización de pomodoro.py para llamar a la configuración al inicio.
  - Actualización del README.md y asistencia_ia.md con la nueva fase.
- Preguntas para la IA:
  - "¿Cómo creo un archivo de configuración en Python con variables globales?"
  - "¿Cómo valido que un número sea positivo y mayor que cero?"
- Respuestas de la IA:
  - Para crear un archivo de configuración con variables globales: Define las variables en un módulo separado (como config.py). Usa `global` dentro de funciones si necesitas modificarlas. Importa las variables en otros módulos con `from config import VARIABLE`.
  - Para validar un número positivo y mayor que cero: Usa un bucle `while True` con `try-except` para convertir a `float`. Verifica `if value > 0`, y repite la solicitud si no es válido.
- Modificaciones realizadas: Agregada función configure() con input validado, y llamada en el main.