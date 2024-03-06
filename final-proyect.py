#La funcion se usa como parametro de funcion de ordenacion para ordenar la lista
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    #El diccionario utiliza nombres de máquinas como claves y conjuntos de usuarios como valores.
    machines = {}
    """iteracion a traves de la lista de eventos
    Los eventos de inicio de sesión agregan usuarios al conjunto, 
    mientras que los eventos de cierre de sesión los eliminan."""
    for event in events:
        #comprobar si la maquina esta en el diccionario,sino, se agrega con valor vacio
        if event.machine not in machines:
            machines[event.machine]= set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type =="logout":
            machines[event.machine].remove(event.user)
    return machines

"""Solo imprime máquinas con usuarios 
actualmente conectados."""
def generate_report(machines):
    for machine, users in machines.items():
        if len (users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
