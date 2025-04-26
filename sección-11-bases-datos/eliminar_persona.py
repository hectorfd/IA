# eliminar persona desde python a Mysql
import mysql.connector

personas = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="personas_db"
)

# ejecutar delete
cursor = personas.cursor()
sentencia_sql = "DELETE FROM personas WHERE id = %s"
valores = (6,)

cursor.execute(sentencia_sql, valores)
personas.commit()
# Cerrar conexión
cursor.close()
personas.close()
