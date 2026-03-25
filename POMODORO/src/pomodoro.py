# pomodoro.py
# Este es el archivo principal del temporizador Pomodoro.
# Gestiona el ciclo de trabajo y descanso, utilizando los módulos de configuración y notificaciones.

import os
import time
import platform
import sys
import threading

from config import WORK_TIME, BREAK_TIME, LONG_BREAK_TIME, TOTAL_CYCLES, configure
from notificaciones import notify_work_start, notify_work_end, notify_break_start, notify_break_end, play_final_beep

# Eventos control para pausar/reanudar y salir
pause_event = threading.Event()
exit_event = threading.Event()

# Función para contar el tiempo en segundos. Muestra el tiempo restante en formato MM:SS.
def draw_progress_bar(elapsed, total, width=30):
    progress = min(max(elapsed / total, 0), 1)
    filled = int(progress * width)
    bar = '█' * filled + '-' * (width - filled)
    return f"[{bar}] {int(progress*100):3d}%"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def countdown(minutes):
    """
    Realiza una cuenta regresiva para el número de minutos especificado.
    Muestra el tiempo restante en la terminal y barra de progreso.
    :param minutes: Número de minutos para la cuenta regresiva
    """
    total_seconds = int(minutes * 60)
    elapsed = 0

    while total_seconds > 0 and not exit_event.is_set():
        if pause_event.is_set():
            print("[PAUSADO] Presiona 'p' para reanudar...           ", end='\r')
            time.sleep(0.5)
            continue

        mins, secs = divmod(total_seconds, 60)
        timer = f'{int(mins):02d}:{int(secs):02d}'
        progress = draw_progress_bar(elapsed, int(minutes * 60))
        print(f"{progress} {timer}", end='\r')
        time.sleep(1)
        total_seconds -= 1
        elapsed += 1

    if exit_event.is_set():
        return

    print("00:00", end='\n')



def keyboard_listener():
    """Escucha teclas en segundo plano para controlar pausa/reanudar/salir."""
    system = platform.system()
    if system != 'Windows':
        import select

    print("Controles: 'p' pausar/reanudar, 'q' salir")

    while not exit_event.is_set():
        key = None

        if system == 'Windows':
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getwch()
        else:
            import select
            if select.select([sys.stdin], [], [], 0.2)[0]:
                key = sys.stdin.read(1)

        if not key:
            time.sleep(0.1)
            continue

        if key.lower() == 'p':
            if pause_event.is_set():
                pause_event.clear()
                print("\n***** Reanudado *****")
            else:
                pause_event.set()
                print("\n***** Pausado *****")

        elif key.lower() == 'q':
            exit_event.set()
            print("\n***** Saliendo... *****")
            break


def show_menu():
    while True:
        clear_screen()
        print("=== Temporizador Pomodoro interactivo ===")
        print("1) Configurar sesión")
        print("2) Iniciar sesión")
        print("3) Salir")
        choice = input("Selecciona una opción (1-3): ").strip()

        if choice == '1':
            configure()
            input("Configuración guardada. Presiona Enter para volver al menú...")
        elif choice == '2':
            clear_screen()
            print("Iniciando temporizador... (p=pausa/reanudar, q=salir)")
            return
        elif choice == '3':
            exit(0)
        else:
            print("Opción inválida. Intenta de nuevo.")
            time.sleep(1)


# Función principal para ejecutar el ciclo Pomodoro
def run_pomodoro():
    """
    Ejecuta el ciclo finito de Pomodoro hasta completar el número configurado de ciclos.
    Incluye descanso largo cada 4 ciclos y muestra estadísticas.
    """
    cycle = 1
    while cycle <= TOTAL_CYCLES[0] and not exit_event.is_set():
        print(f"\n--- Ciclo {cycle} ---")

        # Período de trabajo
        notify_work_start()
        countdown(WORK_TIME[0])
        if exit_event.is_set():
            break
        notify_work_end()

        # Período de descanso: largo cada 4 ciclos
        if cycle % 4 == 0:
            print(f"¡Descanso largo después de {cycle} pomodoros!")
            notify_break_start()
            countdown(LONG_BREAK_TIME)
            if exit_event.is_set():
                break
            notify_break_end()
        else:
            notify_break_start()
            countdown(BREAK_TIME[0])
            if exit_event.is_set():
                break
            notify_break_end()

        # Mostrar estadísticas
        print(f"Estadísticas: Pomodoros completados: {cycle}")

        cycle += 1

    if not exit_event.is_set():
        # Resumen final
        print(f"\n¡Sesión completada! Total de pomodoros: {TOTAL_CYCLES[0]}")
        play_final_beep()
        print("Presiona Enter para salir.")
        input()
    else:
        print("\nTemporizador finalizado antes de completar todos los ciclos.")


# Punto de entrada del programa
if __name__ == "__main__":
    print("Bienvenido al Temporizador Pomodoro")

    show_menu()

    listener_thread = threading.Thread(target=keyboard_listener, daemon=True)
    listener_thread.start()

    try:
        run_pomodoro()
    except KeyboardInterrupt:
        exit_event.set()
        print("\nTemporizador detenido por el usuario.")
    finally:
        exit_event.set()
        listener_thread.join(timeout=1)
