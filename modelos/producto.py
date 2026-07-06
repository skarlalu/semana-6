class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        self.__precio = 0.0
        self.cambiar_precio(precio)
        self.disponible = disponible

    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"⚠️ Error: El precio para '{self.nombre}' debe ser mayor a 0.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"