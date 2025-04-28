from cliente import Cliente
from conexion import Conexion
# DAO es Data Access Object, sirve para acceder a los datos de la base de datos.
# DAO se usa para que no uses directamente sentencias SQL como SELECT, INSERT, UPDATE, DELETE en nuestra logica de negocio
# DAO permite centralizar las operaciones de la base de datos, de esa forma cuando cambies de base de datos por ejemplo de mysql a postgres o oracle, solo tendras que cambiar el DAO de la capa de datos
class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM clientes ORDER id'
    INSERTAR = 'INSERT INTO clientes (nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE clientes SET nombre = %s, apellido = %s, membresia = %s WHERE id = %s'
    ELIMINAR = 'DELETE FROM clientes WHERE id = %s'
    
    @classmethod
    # este es el cliente DAO para seleccionar todos los clientes
    def seleccionar(cls):
        conexion = None
        try:
            # llamamamos a la funcion obtener?conexion de la clase Conexion
            conexion = Conexion.obtener_conexion()
            # cursor() es un objeto que nos permite ejecutar sentencias SQL
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR) # aqui se ejecuta la sentencia que definimos arriba
            # fetchall es un metodo de python que devuelve todos los registros de la consulta
            registros = cursor.fetchall()
            # usamos una lista porque el cursor nos devuelve un iterable
            clientes = []
            # Mapeo de registros de la clase tabla cliente
            # hacemos un for para recorrer todos los registros
            for registro in registros:
                # aqui obtenemos un registro de la tabla cliente
                # registro[0], [1], [2], [3] son los indices de la tupla
                # representan, id, nombre, apellido y membresia
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes# retornamos la lista de clientes, para que pueda ser usada en el codigo
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
            raise
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
                
                
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            print(f'Ocurrio un error al insertar clientes: {e}')
            raise
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
                
    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            print(f'Ocurrio un error al actualizar clientes: {e}')
            raise
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
                
                
    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            print(f'Ocurrio un error al eliminar clientes: {e}')
            raise
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)