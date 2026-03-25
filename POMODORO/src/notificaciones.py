# notificaciones.py
# Este módulo maneja las notificaciones y sonidos del temporizador.
# Utiliza winsound para reproducir sonidos en Windows y print para notificaciones en terminal.

import os
import winsound

# Función para reproducir un sonido de notificación usando Beep
def play_sound(sound_type):
    """
    Reproduce un sonido de beep según el tipo.
    :param sound_type: Tipo de sonido ('work_start', 'work_end', 'break_start', 'break_end')
    """
    if sound_type == 'work_start':
        winsound.Beep(1000, 500)  # Beep alto para inicio de trabajo
    elif sound_type == 'work_end':
        winsound.Beep(800, 500)   # Beep medio para fin de trabajo
    elif sound_type == 'break_start':
        winsound.Beep(600, 500)  # Beep bajo para inicio de descanso
    elif sound_type == 'break_end':
        winsound.Beep(1000, 500)  # Beep alto para fin de descanso
    else:
        winsound.Beep(500, 500)  # Beep por defecto

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
    play_sound('work_start')

# Función para notificar el fin de un período de trabajo
def notify_work_end():
    show_notification("¡Tiempo de trabajo terminado! Toma un descanso.")
    play_sound('work_end')

# Función para notificar el inicio de un descanso
def notify_break_start():
    show_notification("¡Comienza el descanso!")
    play_sound('break_start')

# Función para notificar el fin de un descanso
def notify_break_end():
    show_notification("¡Descanso terminado! Vuelve al trabajo.")
    play_sound('break_end')