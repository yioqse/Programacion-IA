# notificaciones.py
# Este módulo maneja las notificaciones y sonidos del temporizador.
# Utiliza winsound para Windows y \a para otros sistemas, con mensajes destacados.

import platform

# Función para reproducir un sonido de beep usando Beep o \a
def play_sound(sound_type):
    """
    Reproduce un sonido de beep según el tipo y sistema operativo.
    :param sound_type: Tipo de sonido ('work_start', 'work_end', 'break_start', 'break_end')
    """
    system = platform.system()
    if system == 'Windows':
        import winsound
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
    else:
        # Para Linux/Mac, usar el beep de terminal
        print('\a', end='', flush=True)

# Función para mostrar una notificación destacada en la terminal
def show_notification(message):
    """
    Muestra un mensaje de notificación destacado en la terminal.
    :param message: El mensaje a mostrar
    """
    # ANSI escape code para negrita y color amarillo
    print(f"\033[1;33m*** NOTIFICACIÓN: {message} ***\033[0m")

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

# Función para emitir un beep final al terminar la sesión
def play_final_beep():
    """
    Emite un beep al finalizar todos los ciclos.
    """
    system = platform.system()
    if system == 'Windows':
        import winsound
        winsound.Beep(1200, 1000)  # Beep largo y alto
    else:
        print('\a\a', end='', flush=True)  # Doble beep