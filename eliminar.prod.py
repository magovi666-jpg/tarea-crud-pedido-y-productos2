
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

id_producto = int(input("Ingrese el ID del producto a eliminar: "))

cursor.execute(
    "DELETE FROM productos WHERE id_producto = %s",
    (id_producto,)
)

conexion.commit()

if cursor.rowcount > 0:
    print("Producto eliminado correctamente")
else:
    print("No se encontro el producto")

cursor.close()
conexion.close()
