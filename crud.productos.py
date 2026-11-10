import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="comercio",
    user="postgres",
    password="kibaymichifu",
)
print("Conexión exitosa a la base de datos")

cursor = conexion.cursor()

cursor.execute(
    "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
    ("Teclado", 150000, 20)
)

conexion.commit()

print("Producto insertado correctamente")

cursor.close()
conexion.close()

import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="comercio",
    user="postgres",
    password="kibaymichifu",
)

cursor = conexion.cursor()

cursor.execute(
    "SELECT * FROM productos ORDER BY id_producto"
)

productos = cursor.fetchall()

print("\n===== LISTA DE PRODUCTOS =====")

for producto in productos:
    print(producto)

cursor.close()
conexion.close()


import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="comercio",
    user="postgres",
    password="kibaymichifu",
    options="-c lc_messages=C"
)

print("Conexion exitosa a la base de datos")

cursor = conexion.cursor()

print("\n===== MODIFICAR PRODUCTO =====")

id_producto = int(input("Ingrese el ID del producto: "))
nuevo_precio = float(input("Ingrese el nuevo precio: "))

cursor.execute(
    "UPDATE productos SET precio = %s WHERE id_producto = %s",
    (nuevo_precio, id_producto)
)

conexion.commit()

if cursor.rowcount > 0:
    print("Producto modificado correctamente")
else:
    print("No se encontro ningun producto con ese ID")

cursor.close()
conexion.close()


import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="comercio",
    user="postgres",
    password="TU_CONTRASEÑA",
    options="-c lc_messages=C"
)

print("Conexion exitosa a la base de datos")

cursor = conexion.cursor()

print("\n===== ELIMINAR PRODUCTO =====")

id_producto = int(input("Ingrese el ID del producto a eliminar: "))

cursor.execute(
    "DELETE FROM productos WHERE id_producto = %s",
    (id_producto,)
)

conexion.commit()

if cursor.rowcount > 0:
    print("Producto eliminado correctamente")
else:
    print("No se encontro ningun producto con ese ID")

cursor.close()
conexion.close()
