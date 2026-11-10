
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

print("\n===== MODIFICAR PEDIDO =====")

id_pedido = int(input("Ingrese el ID del pedido a modificar: "))
nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

cursor.execute(
    """
    UPDATE pedidos
    SET cantidad = %s
    WHERE id_pedido = %s
    """,
    (nueva_cantidad, id_pedido)
)

conexion.commit()

if cursor.rowcount > 0:
    print("Pedido modificado correctamente")
else:
    print("No se encontro ningun pedido con ese ID")

cursor.close()
conexion.close()
