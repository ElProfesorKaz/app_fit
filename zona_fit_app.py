from cliente import Cliente
from cliente_dao import ClienteDAO


print("***** Zona Fit App **")
print("***** Bienvenido *****")
opcion = None
while opcion != 5:
    print(f"""Menu de opciones: 
    1. Listar clientes 
    2. Agregar clientes
    3. Modificar clientes
    4. Eliminar clientes
    5. Salir""")
    opcion = int(input("Seleccione una opción(1-5): "))
    
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print("***Listado de clientes***")
        for cliente in clientes:
            print(cliente)
    
    elif opcion == 2:
        nombre_var = input("Ingrese el nombre del cliente: ")
        apellido_var = input("Ingrese el apellido del cliente: ")
        membresia_var = input("Ingrese la membresía del cliente: ")
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        cliente_insertado = ClienteDAO.insertar(cliente)
        print(f"Cliente insertado: {cliente_insertado}")
    
    elif opcion == 3:
        id_var = input("Ingrese el id del cliente a modificar: ")
        nombre_var = input("Ingrese el nuevo nombre del cliente: ")
        apellido_var = input("Ingrese el nuevo apellido del cliente: ")
        membresia_var = input("Ingrese la nueva membresía del cliente: ")
        cliente = Cliente(id=id_var, nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f"Cliente actualizado: {clientes_actualizados}")

    elif opcion == 4:
        id_var = input("Ingrese el id del cliente a eliminar: ")
        cliente = Cliente(id=id_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f"Cliente eliminado: {clientes_eliminados}")
else:
        print("Saliendo de la aplicación...")     
        
