# notificaciones.py
# Este módulo maneja las notificaciones y sonidos del temporizador.
# Utiliza la biblioteca playsound para reproducir sonidos y print para notificaciones en terminal.

import os
from playsound import playsound

# Función para reproducir un sonido de notificación
def play_sound(sound_file):
    """
    Reproduce un archivo de sonido.
    :param sound_file: Ruta al archivo de sonido (ej. 'beep.wav')
    """
    if os.path.exists(sound_file):
        playsound(sound_file)
    else:
        print(f"Archivo de sonido no encontrado: {sound_file}")

# Función para mostrar una notificación en la terminal
def show_notification(message):
    """
    Muestra un mensaje de notificación en la terminal.
    :param message: El mensaje a mostrar
    """
    print(f"\n*** NOTIFICACIÓN: {message} ***\n")

# Función para notificar el inicio de un período de trabajo
def notify_work_start():
    show_notification("¡Comienza el tiempo de trabajo!")
    play_sound('sounds/work_start.wav')  # Asumiendo que hay archivos de sonido

# Función para notificar el fin de un período de trabajo
def notify_work_end():
    show_notification("¡Tiempo de trabajo terminado! Toma un descanso.")
    play_sound('sounds/work_end.wav')

# Función para notificar el inicio de un descanso
def notify_break_start():
    show_notification("¡Comienza el descanso!")
    play_sound('sounds/break_start.wav')

# Función para notificar el fin de un descanso
def notify_break_end():
    show_notification("¡Descanso terminado! Vuelve al trabajo.")
    play_sound('sounds/break_end.wav')