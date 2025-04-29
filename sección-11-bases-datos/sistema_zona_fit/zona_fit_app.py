from cliente_dao import ClienteDAO
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
    
        