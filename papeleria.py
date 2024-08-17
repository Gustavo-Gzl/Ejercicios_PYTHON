class ArticuloPapeleria:
    def __init__(self, tipo, especif, precio_compra):
        self.tipo = tipo
        self.especificacion = especif
        self.precio_compra = precio_compra
        self.marca = "HOJITAS" if tipo == "Cuaderno" else "RAYAS"
        self.precio_venta = precio_compra * 1.30 #margen de ganancia

    def mostrar(self):
        print(f"Tipo: {self.tipo}")
        print(f"Especificación: {self.especificacion}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")

# datos a imprimir
cuaderno = ArticuloPapeleria("Cuaderno", "100 hojas", 2.50)
lapiz = ArticuloPapeleria("Lápiz", "Grafito", 0.50)

cuaderno.mostrar()
lapiz.mostrar()
