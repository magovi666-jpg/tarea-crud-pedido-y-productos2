import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="comercio",
    user="postgres",
    password="kibaymichifu"
)
print("Conexión exitosa a la base de datos")

cursor = conexion.cursor()
cursor.execute(
    "INSERT INTO clientes (nombre, email, ciudad) VALUES (%s, %s, %s)",
    ("Pedro Lopez", "pedro@mail.com", "Capiata")
)
conexion.commit()
print("Cliente insertado correctamente")


import psycopg2

try:
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

except Exception as error:
    print("Error:", error)
