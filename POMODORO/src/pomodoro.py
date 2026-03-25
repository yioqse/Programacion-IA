# pomodoro.py
# Este es el archivo principal del temporizador Pomodoro.
# Gestiona el ciclo de trabajo y descanso, utilizando los módulos de configuración y notificaciones.

import time
from config import WORK_TIME, BREAK_TIME, LONG_BREAK_TIME, TOTAL_CYCLES, configure
from notificaciones import notify_work_start, notify_work_end, notify_break_start, notify_break_end, play_final_beep

# Función para contar el tiempo en segundos. Muestra el tiempo restante en formato MM:SS.
def countdown(minutes):
    """
    Realiza una cuenta regresiva para el número de minutos especificado.
    Muestra el tiempo restante en la terminal.
    :param minutes: Número de minutos para la cuenta regresiva
    """
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{int(mins):02d}:{int(secs):02d}'
        print(timer, end='\r')  # Imprime en la misma línea
        time.sleep(1)
        total_seconds -= 1
    print("00:00")  # Cuando termina

# Función principal para ejecutar el ciclo Pomodoro
def run_pomodoro():
    """
    Ejecuta el ciclo finito de Pomodoro hasta completar el número configurado de ciclos.
    Incluye descanso largo cada 4 ciclos y muestra estadísticas.
    """
    cycle = 1
    while cycle <= TOTAL_CYCLES[0]:
        print(f"\n--- Ciclo {cycle} ---")
        
        # Período de trabajo
        notify_work_start()
        countdown(WORK_TIME[0])
        notify_work_end()
        
        # Período de descanso: largo cada 4 ciclos
        if cycle % 4 == 0:
            print(f"¡Descanso largo después de {cycle} pomodoros!")
            notify_break_start()
            countdown(LONG_BREAK_TIME)
            notify_break_end()
        else:
            notify_break_start()
            countdown(BREAK_TIME[0])
            notify_break_end()
        
        # Mostrar estadísticas
        print(f"Estadísticas: Pomodoros completados: {cycle}")
        
        cycle += 1
    
    # Resumen final
    print(f"\n¡Sesión completada! Total de pomodoros: {TOTAL_CYCLES[0]}")
    play_final_beep()
    print("Presiona Enter para salir.")
    input()

# Punto de entrada del programa
if __name__ == "__main__":
    print("Bienvenido al Temporizador Pomodoro")
    configure()  # Configurar tiempos personalizables
    print("Presiona Ctrl+C para detener en cualquier momento.")
    run_pomodoro()