
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

cursor.execute("""
        SELECT * FROM pedidos
        ORDER BY id_pedido;
""")

pedidos = cursor.fetchall()

print("\n===== LISTA DE PEDIDOS =====")

if pedidos:
    for pedido in pedidos:
            print(pedido)
else:
        print("No hay pedidos registrados.")

cursor.close()
conexion.close()


