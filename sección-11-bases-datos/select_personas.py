import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="personas_db"
)

# Crear un cursor
cursor = conexion.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM personas")
# Recuperar resultados
resultados = cursor.fetchall()
# Imprimir resultados
for resultado in resultados:
    print(resultado)

# Cerrar conexión
cursor.close()
conexion.close()