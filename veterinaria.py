class Perro:    
    def __init__(self, nombre, raza, edad, color, peso, dueño, telefono):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso
        self.dueño = dueño
        self.telefono = telefono
        self.estado = "NO ATENDIDO"
    
    def registrar(self):
        self.estado = "ATENDIDO"
        tamaño = "Perro Grande" if self.peso > 15 else "Perro Pequeño"
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso} kg - {tamaño}")
        print(f"Dueño: {self.dueño}")
        print(f"Teléfono: {self.telefono}")
        print(f"Estado: {self.estado}")

# Ejemplo de uso
perro1 = Perro("Ragnar", "Dogo Argentino", 3, "Negro", 35 , "Elmer Gustavo", "7315-1920")
perro1.registrar()
