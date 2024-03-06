# Final-Proyect-Crash-Of-Python---Google-IT-Automation

# Seguimiento de Eventos de Inicio y Cierre de Sesión

Este código proporciona funciones para seguir eventos de inicio y cierre de sesión en máquinas, así como para generar un informe de las máquinas con usuarios actualmente conectados.

## Funciones Principales

### `get_event_date(event)`

Esta función se utiliza como clave de ordenación para ordenar la lista de eventos según la fecha.

### `current_users(events)`

Esta función toma una lista de eventos, los ordena por fecha y luego realiza un seguimiento de los usuarios actuales en cada máquina. Utiliza un diccionario donde las claves son nombres de máquinas y los valores son conjuntos de usuarios. Los eventos de inicio de sesión agregan usuarios al conjunto, mientras que los eventos de cierre de sesión los eliminan.

### `generate_report(machines)`

Esta función imprime un informe de las máquinas con usuarios actualmente conectados. Itera a través del diccionario de máquinas y usuarios, solo imprime máquinas con usuarios.

## Clase `Event`

La clase `Event` se utiliza para representar eventos de inicio y cierre de sesión. Cada evento tiene una fecha, un tipo (inicio o cierre de sesión), el nombre de la máquina y el nombre de usuario asociado.

## Ejemplo de Uso

Se proporciona una lista de eventos de ejemplo, y se demuestra cómo utilizar las funciones para obtener un diccionario de máquinas y usuarios actuales, así como generar e imprimir un informe.

```python
# Crear eventos de ejemplo
events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  # ... (otros eventos)
]

# Obtener usuarios actuales
users = current_users(events)
print(users)

# Generar e imprimir un informe de máquinas con usuarios actuales
generate_report(users)
