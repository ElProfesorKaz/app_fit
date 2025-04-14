from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = "zona_fit_db"
    USERNAME = "root"
    PASSWORD = "admin"
    HOST = "localhost"
    PORT = "3306"
    POOL_SIZE = 5
    POOL_NAME = "zona_fit_pool"
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    port=cls.PORT
                )
                print("Pool de conexiones creado con éxito.")
                return cls.pool
        
            except Error as e:
                print(f"Error al crear el pool de conexiones: {e}")
        else:
            return cls.pool
    
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        return conexion.close()

if __name__ == "__main__":
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print("Conexión liberada.")