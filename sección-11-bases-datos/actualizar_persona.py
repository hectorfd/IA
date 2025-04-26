# actualizar persona desde python a Mysql
import mysql.connector

personas = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="personas_db"
)
# ejecutar update
cursor = personas.cursor()
sentencia_sql = "UPDATE personas SET apellido = %s WHERE id = %s"
valores = ('Ferro Dávalos', 1)

cursor.execute(sentencia_sql, valores)
personas.commit()
# Cerrar conexión
cursor.close()
personas.close()
