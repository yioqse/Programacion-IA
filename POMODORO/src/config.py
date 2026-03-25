# config.py
# Este archivo contiene las configuraciones del temporizador Pomodoro.
# Aquí se definen los tiempos de trabajo y descanso, así como otras constantes.

# Valores por defecto
DEFAULT_WORK_TIME = 25
DEFAULT_BREAK_TIME = 5

# Tiempo de trabajo en minutos (usando lista para mutabilidad)
WORK_TIME = [DEFAULT_WORK_TIME]

# Tiempo de descanso en minutos (usando lista para mutabilidad)
BREAK_TIME = [DEFAULT_BREAK_TIME]

# Número de ciclos Pomodoro antes de un descanso largo (opcional)
CYCLES_BEFORE_LONG_BREAK = 4

# Tiempo de descanso largo en minutos
LONG_BREAK_TIME = 15

def get_positive_float(prompt, default):
    """
    Solicita al usuario un número flotante positivo mayor que cero.
    :param prompt: Mensaje a mostrar al usuario
    :param default: Valor por defecto si el usuario no ingresa nada
    :return: Número flotante válido
    """
    while True:
        try:
            value = input(f"{prompt} (por defecto {default}): ").strip()
            if not value:
                return default
            value = float(value)
            if value > 0:
                return value
            else:
                print("El valor debe ser un número positivo mayor que cero.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def configure():
    """
    Permite al usuario configurar los tiempos de trabajo y descanso.
    Actualiza las listas WORK_TIME y BREAK_TIME.
    """
    print("\n--- Configuración del Temporizador Pomodoro ---")
    WORK_TIME[0] = get_positive_float("Ingresa el tiempo de trabajo en minutos", DEFAULT_WORK_TIME)
    BREAK_TIME[0] = get_positive_float("Ingresa el tiempo de descanso en minutos", DEFAULT_BREAK_TIME)
    print(f"Configuración actualizada: Trabajo = {WORK_TIME[0]} min, Descanso = {BREAK_TIME[0]} min\n")