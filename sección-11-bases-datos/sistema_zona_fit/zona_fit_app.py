from cliente_dao import ClienteDAO
from cliente import Cliente
print('Zona Fit')
option = None
while option != 5:
    print(f'''Menu:
        1. Listar Clientes
        2. Agregar Clientes
        3. Modificar Clientes
        4. Eliminar Clientes
        5. Salir''')
    option = int(input('Seleccione una opción: '))
    if option == 1:
        clientes = ClienteDAO.seleccionar()
        print('Listado de Clientes: ')
        for cliente in clientes:
            print(cliente)
    elif option == 2:
        nombre_var = input('Ingrese el nombre: ')
        apellido_var = input('Ingrese el apellido: ')
        membresia_var = int(input('Ingrese la membresia: '))
        cliente = Cliente(nombre = nombre_var, apellido = apellido_var, membresia = membresia_var)
        ClienteDAO.insertar(cliente)
        print('Cliente insertado correctamente')
    elif option == 3:
        id_var = int(input('Ingrese el id: '))
        nombre_var = input('Ingrese el nombre: ')
        apellido_var = input('Ingrese el apellido: ')
        membresia_var = int(input('Ingrese la membresia: '))
        cliente = Cliente(id = id_var, nombre = nombre_var, apellido = apellido_var, membresia = membresia_var)
        ClienteDAO.actualizar(cliente)
        print('Cliente actualizado correctamente')
        
    
        