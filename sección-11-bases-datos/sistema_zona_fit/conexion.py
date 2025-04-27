from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = '12345678'
    HOST = 'localhost'
    DB_PORT = 3306
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    _pool = None  # Usamos convención de _ para atributo "privado"
    
    # este metodo e clase priado nos permite crear un pool de conexiones mas eficiente
    # los metodos privados no se pueden acceder desde fuera de la clase
    @classmethod
    def _crear_pool(cls):
        try:
            # no guardamos el pooling en una variable sino que la retornamos directamente
            return pooling.MySQLConnectionPool(
                pool_name=cls.POOL_NAME,
                pool_size=cls.POOL_SIZE,
                host=cls.HOST,
                user=cls.USERNAME,
                port=cls.DB_PORT,
                password=cls.PASSWORD,
                database=cls.DATABASE
            )
        except Error as e:# Error es una clase de mysql.connector que nos permite manejar errores
            print(f'Error al crear el pool de conexiones: {e}')
            raise # recomendamos usar raise para identificar el error
        
    # este metodo es para acceder al pool de conexiones
    # si el pool no existe o es none, lo crea
    @classmethod
    def obtener_pool(cls):
        # Versión más concisa usando or (evalúa cls._pool primero, si es None, ejecuta _crear_pool)
        cls._pool = cls._pool or cls._crear_pool()
        return cls._pool
    
    @classmethod
    def obtener_conexion(cls):
        try:
            return cls._pool.get_connection()# get_connection es un metodo de mysql
        except Erro as e:
            print(f'Error al otener la conexión: {e}')
            raise
    
    @classmethod
    def liberar_conexion(cls, conexion):# conexion es un parametro que se usara mas adelante para cerrar la conexion
        conexion.close()