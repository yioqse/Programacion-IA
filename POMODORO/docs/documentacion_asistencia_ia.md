# Documentación de Asistencia IA

Este documento complementa `asistencia_ia.md` para documentar el uso del temporizador Pomodoro con ejemplos prácticos.

## Ejecución básica

1. Abrir terminal en la carpeta del proyecto:

   ```bash
   cd c:\Users\IA\Documents\Programacion-IA\POMODORO
   ```

2. Ejecutar:

   ```bash
   python src/pomodoro.py
   ```

3. En el menú:
   - 1) Configurar sesión
   - 2) Iniciar sesión
   - 3) Salir

4. Controles mientras corre el temporizador:
   - `p`: Pausar / reanudar
   - `q`: Finalizar la sesión anticipadamente

## Ejemplo de configuración

Durante la opción 1, ingresa:

- Tiempo de trabajo: 2 (minutos)
- Tiempo de descanso: 1 (minutos)
- Ciclos a completar: 3

Luego selecciona 2 para iniciar.

## Comportamiento de la sesión

- Se muestra una barra de progreso en cada bloque de tiempo.
- Cada 4 ciclos se usa descanso largo de 15 minutos.
- Al finalizar todos los ciclos se emite un beep final y se muestra un resumen.

## Notas

- El código soporta Windows/Linux/macOS para beep y limpieza de pantalla.
- Se utiliza `asistencia_ia.md` para registrar el proceso de desarrollo paso a paso.
