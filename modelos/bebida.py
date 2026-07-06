from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, tamano_ml: int, disponible: bool = True):
        super().__init__(nombre, precio, disponible)
        self.tamano_ml = tamano_ml

    def mostrar_informacion(self):
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Tamaño: {self.tamano_ml} ml"