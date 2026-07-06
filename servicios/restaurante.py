class Restaurante:
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento = nombre_establecimiento
        self.inventario_productos = []

    def agregar_producto(self, producto):
        self.inventario_productos.append(producto)
        print(f"✅ Registrado exitosamente: {producto.nombre}")

    def mostrar_menu_completo(self):
        print(f"\n--- MENÚ DEL RESTAURANTE: {self.nombre_establecimiento.upper()} ---")
        if not self.inventario_productos:
            print("El menú se encuentra vacío en este momento.")
            return

        for producto in self.inventario_productos:
            print(producto.mostrar_informacion())
        print("-" * 50)