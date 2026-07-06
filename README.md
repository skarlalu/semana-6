Estudiante:Karla Daniela Luque Navarrete 
Asignatura: Programación Orientada a Objetos (Semana 6)

Este sistema es una solución de software modular en Python diseñada para gestionar los productos disponibles dentro de un restaurante. Permite registrar diferentes elementos de consumo clasificándolos de forma lógica y estructurada, garantizando la persistencia temporal de la información en memoria a través de capas de servicios bien diferenciadas.

El proyecto sigue una arquitectura limpia y modular separando datos/modelos de la lógica del negocio:

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

Principios de POO Aplicados
Herencia
Se implementó una jerarquía clara donde la clase padre Producto unifica los atributos compartidos por cualquier artículo del menú (nombre, precio, disponibilidad). Las clases hijas Platillo y Bebida heredan estos comportamientos mediante el uso de la función super(), permitiendo expandir características específicas como tiempo_preparacion y tamano_ml respectivamente, evitando la duplicidad de código.

Encapsulación
Para resguardar la integridad financiera de los productos, el atributo precio fue completamente encapsulado definiéndolo de forma privada como __precio. El acceso o lectura externa se realiza de manera controlada por el método obtener_precio(), mientras que las modificaciones se gestionan mediante cambiar_precio(), el cual valida estrictamente que ningún precio asignado sea menor o igual a cero.

Polimorfismo
El polimorfismo se hace presente a través de la sobrescritura del método mostrar_informacion(). Al iterar sobre la lista genérica de productos dentro del servicio Restaurante, el programa ejecuta la misma llamada del método sobre todos los elementos, pero cada objeto dinámicamente decide cómo formatear y entregar su propia cadena de texto dependiendo de su tipo en tiempo de ejecución.