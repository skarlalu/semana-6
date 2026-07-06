from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def ejecutar_sistema():
    mi_restaurante = Restaurante("Gourmet Modular")

    platillo1 = Platillo("Lomo Saltado", 12.50, 20)
    platillo2 = Platillo("Ceviche Clásico", 15.00, 15)

    bebida1 = Bebida("Chicha Morada Grande", 3.50, 500)
    bebida2 = Bebida("Limonada Frozen", 4.00, 400)

    print("--- REGISTRANDO PRODUCTOS ---")
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    mi_restaurante.mostrar_menu_completo()

    print("\n--- PRUEBAS DE ENCAPSULACIÓN Y VALIDACIÓN ---")
    print(f"Precio actual de {platillo1.nombre}: ${platillo1.obtener_precio():.2f}")
    
    print("\nIntentando cambiar el precio a un valor negativo (-5.00)...")
    platillo1.cambiar_precio(-5.00)
    
    print("\nIntentando cambiar el precio a un valor correcto (13.99)...")
    platillo1.cambiar_precio(13.99)

    mi_restaurante.mostrar_menu_completo()

if __name__ == "__main__":
    ejecutar_sistema()