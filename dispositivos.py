class DispositivoElectronico:
    def __init__(self, tipo, modelo, especificaciones, sistema_operativo, almacenamiento, precio_compra):
        self.tipo = tipo
        self.modelo = modelo
        self.especificaciones = especificaciones
        self.sistema_operativo = sistema_operativo
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.marca = "PHR"
        self.precio_venta = precio_compra * 1.7 #margen de ganancia
        self.importado = True

    def mostrar(self):
        print(f"Tipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Especificaciones: {self.especificaciones}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print(f"Importado: {self.importado}")

# Ejemplo de uso
celular = DispositivoElectronico("Celular", "SAMSUNG Galaxy S24 Ultra", "Pantalla 6,8 Pulgadas, Resolucion QHD+ (3120 x 1440) 120 Hz", "Android 14", "25G B", 1180)
celular.mostrar()
