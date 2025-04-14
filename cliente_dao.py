from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    INSERTAR = "INSERT INTO cliente(nombre,apellido, membresia) VALUES(%s, %s,%s)"
    ACTUALIZAR = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM cliente WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error al seleccionar clientes: {e}")
        
        finally:
            if conexion is not None:
                cursor.close()
                conexion.close()

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount  # Retorna el número de filas afectadas
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                conexion.close()

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount  # Retorna el número de filas afectadas
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                conexion.close()

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount  # Retorna el número de filas afectadas
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                conexion.close()


if __name__ == "__main__":
#Insertar clientes
    cliente1 = Cliente(nombre="Juan", apellido="Pérez", membresia="102")
    clientes_actualizados = ClienteDAO.insertar(cliente1)
    print(f"Clientes insertados: {clientes_actualizados}")
#Seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

#Eliminar clientes
    cliente_eliminar = Cliente(id=10)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f"Clientes eliminados: {clientes_eliminados}")

#Actualizar clientes
    cliente_actualizar = Cliente(10, "Carlos", "Gómez", "103")
    cliente_actualizado = ClienteDAO.actualizar(cliente_actualizar)
    print(f"Cliente actualizado: {cliente_actualizado}")