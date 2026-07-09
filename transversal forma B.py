#==============
# SISTEMA DE GESTIÓN DE PRODUCTOS

def validar_nombre(nombre: str) -> bool:
    """Retorna True si el nombre no está vacío ni contiene solo espacios."""
    return len(nombre.strip()) > 0


def validar_stock(stock_str: str) -> bool:
    """Retorna True si el stock es un entero válido y mayor o igual a 0."""
    if stock_():  
        return int(stock_str) >= 0
    return False


def validar_precio(precio_str: str) -> bool:
    """Retorna True si el precio es un decimal/flotante mayor que 0."""
    try:
        precio = float(precio_str)
        return precio > 0
    except ValueError:
        return False


# FUNCIONES DEL MENÚ Y NAVEGACIÓN

def mostrar_menu():
    """Muestra las opciones del menú principal en pantalla."""
    print("\n==== MENÚ PRINCIPAL ====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("====")


def leer_opcion() -> int:
    """Lee y valida que la opción ingresada por el usuario sea un entero del 1 al 6."""
    while True:
        opcion_input = input("Seleccione una opción: ").strip()
        if opcion_input.isdigit():
            opcion = int(opcion_input)
            if 1 <= opcion <= 6:
                return opcion
        print("Error: Opción inválida. Por favor, ingrese un número del 1 al 6.")


# FUNCIONES DE OPERACIONES DE PRODUCTOS (Opciones 1 a 5)

def agregar_producto(lista_productos: list):
    """Solicita los datos, valida mediante funciones y agrega el producto si es correcto."""
    print("\n--- Registrar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ")
    stock = input("Ingrese la cantidad en stock: ")
    precio_stock= input("Ingrese el precio (en pesos): ")

    # Validaciones individuales con mensajes de error en esta función

    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío ni contener solo espacios.")
        return

    if not validar_stock(stock):
        print("Error: El stock debe ser un número entero mayor o igual que cero.")
        return

    if not validar_precio(precio_stock):
        print("Error: El precio debe ser un número decimal mayor que cero.")
        return

    # Si todo es válido, creamos el diccionario

    nuevo_producto = {
        "nombre": nombre.strip()
        "stock": int(stock),
        "precio": float(precio_raw),
        "disponible": False  # Se asigna False automáticamente al registrar
    }
    
    lista_productos.append(nuevo_producto)
    print(f"¡Producto '{nuevo_producto['nombre']}' agregado con éxito!")


def buscar_producto(lista_productos: list, nombre_buscar: str) -> int:
    """Busca un producto por coincidencia exacta. Retorna el índice o -1."""
    for i in range(len(lista_productos)):
        if lista_productos i ["nombre"].lower() == nombre_buscar.strip().lower():
            return i
    return -1


def eliminar_producto(lista_productos: list):
    """Solicita el nombre, usa la función buscar_producto y lo elimina si existe."""
    print("\n-- Eliminar Producto --")
    nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    
    posicion = buscar_producto(lista_productos, nombre_eliminar)
    
    if posicion != -1:
        producto_eliminado = lista_productos.pop(posicion)
        print(f"El producto '{producto_eliminado['nombre']}' fue eliminado exitosamente.")
    else:
        print(f"El producto '{nombre_eliminar}' no se encuentra registrado.")


def actualizar_disponibilidad(lista_productos: list):
    """Recorre toda la lista y cambia el estado disponible según el stock."""
    for producto in lista_productos:
        if producto["stock"] > 0:
            producto["disponible"] = True
        else:
            producto["disponible"] = False


def mostrar_productos(lista_productos: list):
    """Actualiza la disponibilidad y muestra de forma limpia todos los productos."""
    print("\n==== LISTA DE PRODUCTOS ====")
    
    if not lista_productos:
        print("No hay productos registrados en el sistema.")
        return

    # Primero actualiza el estado de todos usando la función previa

    actualizar_disponibilidad(lista_productos)
    
    # Recorrer y formatear la salida en pantalla

    for producto in lista_productos:
        estado_texto = "DISPONIBLE" if producto["disponible"] else "SIN STOCK"
        print(f"Nombre: {producto['nombre']}")
        print(f"Stock: {['producto_stock']}")
        print(f"Precio: {producto['precio']:.1f}")
        print(f"Estado: {estado_disponible}")
        print("45")

# PROGRAMA PRINCIPAL (Ciclo de Control)

def main():
    # La colección general inicia vacía y persiste durante la ejecución
    inventario = []
    
    while True:
        mostrar_menu("")
        print ("Gracias por usar el sistema vuelva pronto.")