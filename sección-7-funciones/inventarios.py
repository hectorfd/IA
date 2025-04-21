print('product inventory')
print('-'*80)
# necesitamos un diccionario vacio para guardar los productos
inventory_dict = {}
def menu():
    print('Mostrar Menu:')
    print(f'\t1. Mostrar inventario:')
    print(f'\t2. Agregar nuevo producto:')
    print(f'\t3. buscar por Id:')
    print(f'\t4. Salir:')
    print('-'*80)
    

def show_inventory(inventario):
    if not inventario:
        print('The inventory is empty')
    else: 
        print('Inventory:')
        for product_id, details in inventario.items():
            print(f'\tID: {product_id}')
            for key, value in details.items():
                print(f'\t\t{key.capitalize()}: {value}')
            print('-'*40)   
            
def add_inventory(inventario):
    print('Add new product')
    product_id = input('Enter ID of product: ')
    if product_id in inventario:
        print(f'This product with Id{product_id} already exist')
    else:
        name = input('Enter the name of the product: ')
        price = float(input('Enter the price of the product: '))
        quantity = int(input('Enter the Quantity: '))
        inventario[product_id] = {
            'name' : name,
            'quantity': quantity,
            'price' : price
        }
        print(f'\t Product with Id {product_id} added at inventory')
def search_inventory(inventario):
    product_id = input(f'\tTngrese el Id del producto: ')
    if product_id in inventario:
        print(f'\t producto encontrado ID:{product_id}:')
        for key, value in inventario[product_id].items():
            print(f'{key.capitalize()}: {value}')

def main():
    while True:
        menu()
        option = int(input('Select an Option: '))
        if option == 1:
            show_inventory(inventory_dict)
        elif option == 2:
            add_inventory(inventory_dict)
        elif option == 3:
            search_inventory(inventory_dict)
        elif option == 4:
            print(f'\tLogging out of the Sistems')
            break
        else: print('\terror')

main()