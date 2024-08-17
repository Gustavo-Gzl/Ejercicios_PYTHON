"""
En un hotel pequeño, los recepcionistas suelen tener dificultades para gestionar 
las reservas de las habitaciones, especialmente cuando deben organizar la 
disponibilidad de las habitaciones y registrar los datos de los huéspedes manualmente. 
Este proceso consume tiempo y puede generar errores humanos al registrar o consultar las reservas. 
Crear un sistema de gestión de reservas para el hotel usando los principios de la Programación 
Orientada a Objetos (POO). El sistema permitirá al recepcionista ingresar las reservas de los huéspedes, 
asignar habitaciones disponibles y mostrar la información de las reservas realizadas.
"""
from datetime import datetime

# Clase Habitacion
"""
Esta clase define los atributos de una habitación, como su número, tipo (simple, doble, suite), 
y su disponibilidad. La clase tiene métodos para asignar y liberar la habitación.
"""
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponible = True
    
    def asignar(self):
        self.disponible = False
    
    def liberar(self):
        self.disponible = True

# Clase Huesped
"""
Esta clase almacena la información de los huéspedes, como el nombre, identificación y contacto.
"""
class Huesped:
    def __init__(self, nombre, identificacion, contacto):
        self.nombre = nombre
        self.identificacion = identificacion
        self.contacto = contacto

# Clase Reserva
"""
Esta clase representa una reserva que relaciona a un huésped con una habitación 
específica y las fechas de entrada y salida.
"""
class Reserva:
    def __init__(self, huesped, habitacion, fecha_entrada, fecha_salida):
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

# Clase Hotel
"""
Esta clase gestiona las habitaciones y reservas del hotel. Tiene métodos para agregar 
habitaciones, hacer una reserva y mostrar las reservas actuales.
"""
class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def hacer_reserva(self, huesped, fecha_entrada, fecha_salida):
        try:
            fecha_entrada_dt = datetime.strptime(fecha_entrada, "%Y-%m-%d")
            fecha_salida_dt = datetime.strptime(fecha_salida, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Por favor, use el formato YYYY-MM-DD.")
            return

        for habitacion in self.habitaciones:
            if habitacion.disponible:
                habitacion.asignar()
                nueva_reserva = Reserva(huesped, habitacion, fecha_entrada_dt, fecha_salida_dt)
                self.reservas.append(nueva_reserva)
                print(f"Reserva exitosa. Habitación {habitacion.numero} asignada.")
                return
        print("No hay habitaciones disponibles.")

    def liberar_habitaciones(self):
        fecha_hoy = datetime.now()
        for reserva in self.reservas:
            if fecha_hoy > reserva.fecha_salida:
                reserva.habitacion.liberar()
                print(f"Habitación {reserva.habitacion.numero} liberada.")

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas.")
            return
        for reserva in self.reservas:
            print(f"*~ Huesped: {reserva.huesped.nombre}\n *~ Habitación: {reserva.habitacion.numero}\n *~ Entrada: {reserva.fecha_entrada.date()}\n *~ Salida: {reserva.fecha_salida.date()}")

# Crear un nuevo hotel y agregar habitaciones
hotel = Hotel()

# Agregar habitaciones al hotel
hotel.agregar_habitacion(Habitacion(10, "Simple"))
hotel.agregar_habitacion(Habitacion(15, "Doble"))
hotel.agregar_habitacion(Habitacion(22, "Suite"))

while True:
    print("\n1. Hacer Reserva")
    print("2. Ver Reservas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Crear un nuevo huésped
        nombre = input("Ingrese el nombre del huésped: ")
        identificacion = input("Ingrese la identificación del huésped: ")
        contacto = input("Ingrese el número de contacto del huésped: ")
        huesped = Huesped(nombre, identificacion, contacto)
        
        # Obtener las fechas de entrada y salida
        fecha_entrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
        fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
        
        # Realizar la reserva
        hotel.hacer_reserva(huesped, fecha_entrada, fecha_salida)

    elif opcion == "2":
        # Mostrar las reservas actuales
        hotel.mostrar_reservas()

    elif opcion == "3":
        # Salir del programa
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")
