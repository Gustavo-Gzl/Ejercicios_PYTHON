class Auto:
    def __init__(self, marca, modelo, año, color, motor, transmision, traccion, tipo_combustible, precio_compra, origen):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor
        self.transmision = transmision
        self.traccion = traccion
        self.tipo_combustible = tipo_combustible
        self.precio_compra = precio_compra
        self.origen = origen
        self.ruedas = 4
        self.capacidad_pasajeros = 5
        self.precio_venta = precio_compra * 1.4 #margen de ganancia

    def mostrar(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmision}")
        print(f"Tracción: {self.traccion}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")

# Ejemplo de uso
auto1 = Auto("Toyota", "Corolla", 2023, "Rojo", "1.8L", "Automática", "FWD", "Gasolina", 20000, "Nacional")
auto1.mostrar()
