from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int, disponible: bool = True):
        super().__init__(nombre, precio, disponible)
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self):
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Tiempo de Prep: {self.tiempo_preparacion} min."