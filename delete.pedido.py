
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

print("\n===== ELIMINAR PEDIDO =====")

id_pedido = int(input("Ingrese el ID del pedido a eliminar: "))

cursor.execute(
    "DELETE FROM pedidos WHERE id_pedido = %s",
    (id_pedido,)
)

conexion.commit()

if cursor.rowcount > 0:
    print("Pedido eliminado correctamente")
else:
    print("No se encontro ningun pedido con ese ID")

cursor.close()
conexion.close()
