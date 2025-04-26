# insertar personas desde python a Mysql
import mysql.connector

personas = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="personas_db"
)
# ejecutar insert

cursor = personas.cursor() # cursor sirve para ejecutar sentencias SQL
# los VALUES tienen que ser iguales a los valores existentes en la tabla
# en este caso se obvia el id porque es auto increment
sentencia_sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
# valores es una tupla, seran los valores que se insertaran en la tabla
valores = ('Pamela', 'Jimenez', 31)
# execute es un metodo de python que ejecuta(sentencia_sql, valores) 
cursor.execute(sentencia_sql, valores)

personas.commit()# el commit es para guardar los cambios en la base de datos
# rowcount es un atributo de python que devuelve el numero de filas afectadas
print(f'Filas insertadas: {cursor.rowcount} -> {valores}')

# Cerrar conexión
cursor.close()
personas.close()