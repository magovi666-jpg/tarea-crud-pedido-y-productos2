import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="comercio",
    user="postgres",
    password="kibaymichifu",
)

print("Conexion exitosa a la base de datos")

cursor = conexion.cursor()

print("\n===== REGISTRAR PEDIDO =====")

id_cliente = int(input("Ingrese el ID del cliente: "))
id_producto = int(input("Ingrese el ID del producto: "))
cantidad = int(input("Ingrese la cantidad: "))
fecha = input("Ingrese la fecha (AAAA-MM-DD): ")

cursor.execute(
    """INSERT INTO pedidos
    (id_cliente, id_producto, cantidad, fecha)
    VALUES (%s, %s, %s, %s)""",
    (id_cliente, id_producto, cantidad, fecha)
)

conexion.commit()

print("Pedido registrado correctamente")

cursor.close()
conexion.close()

