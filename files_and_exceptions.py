def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas_por_producto = {}
    try:
        with open(filename, 'r') as archivo:
            linea = archivo.readline().strip()
            ventas = linea.split(';')
            for venta in ventas:
                if venta:  # Ignora strings vacíos (como el que queda al final del split si termina en ;)
                    producto, valor = venta.split(':')
                    valor = float(valor)
                    if producto not in ventas_por_producto:
                        ventas_por_producto[producto] = []
                    ventas_por_producto[producto].append(valor)
        return ventas_por_producto
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no existe.")


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos) if montos else 0.0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")