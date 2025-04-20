space = 71
print('Inventory management')

def menu():
    print('Menu:')
    print('|1.✍️  Add product', '|2.⛔ Delete product', '|3.🆎 View products', '|4. Exit ❌|')
    print('-' * space)
menu()

product_list = []

def management_inventory():
    option = int(input('Select an option: '))
    if option == 1:
        count_dictionary = int(input('Enter the number of products to add: '))
        if count_dictionary <= 0:
            print('⚠️ Invalid number, try again...')
            management_inventory()
        else:
            for i in range(count_dictionary):
                id = len(product_list) + 1
                print('Add product...')
                name = input(f'Enter the name of product: ').lower().capitalize()
                price = float(input('Enter the price: '))
                quantity = int(input('Enter the quantity: '))
                product_list.append({
                        'id': id,
                        'name': name,
                        'price': price,
                        'quantity': quantity
                })
                print(f'✅ Product {id} added successfully')
                print('-' * space)
            menu()
            management_inventory()
    elif option == 2:
        id = int(input('Enter the ID of the product to delete: '))
        if id > len(product_list) or id <= 0:
            print('⚠️ Product not found, try again...')
            menu()
            management_inventory()
        else:
            print(f'✅ Product {id} deleted successfully')
            del product_list[id - 1]
            menu()
            management_inventory()
    elif option == 3:
        print('View products...')
        print('-' * space)
        for product in product_list:
            print(f'ID: {product["id"]}')
            print(f'  Name: {product["name"]}')
            print(f'  Price: S/. {product["price"]}')
            print(f'  Quantity: {product["quantity"]}')
            print('-' * space)
        menu()
        management_inventory()
    elif option == 4:
        print('Exit...')
        print('-' * space)
        print('Product list:')
        print('-' * space)
        count = 0
        for product in product_list:
            print(f'ID: {product["id"]}')
            print(f'  Name: {product["name"]}')
            print(f'  Price: S/. {product["price"]}')
            print(f'  Quantity: {product["quantity"]}')
            print('-' * space)
            count += 1
            total = sum(producto['price'] * producto['quantity'] for producto in product_list)
        print(f'Total value of products: S/. {total}')
        print(f'Total products: {count}')
        print('Thank you for using the inventory management system!')
        print('-' * space)
        exit()
management_inventory()

