buy = {}
def menu():
    print('-'*90)
    print('Snaks Store Menu:')
    print('\t\t 1. 👀 Show Snaks| 2. 🛒 Buy Snaks | 3. 💰 Show Ticket | 4. ❎ Exit|')
    print('-'*90)

# snaks dictionary
inventory = {
    1:{'name':'Papas fritas','price':2.50,'quantity': 5},
    2:{'name':'Canchita','price':0.50,'quantity': 5},
    3:{'name':'Gaseosa personal','price':2.00,'quantity': 5},
    4:{'name':'empanada','price':1.50,'quantity': 5},
    5:{'name':'galleta','price':1.00,'quantity': 5},
}
# inv = datos del inventario

def show_snaks(inv):
    print('Snaks available')
    for id_snak, details in inv.items():
        print(f'  Id: {id_snak}')
        for key, value in details.items():
            print(f'\t{key.capitalize()}: {value}')
        print('')
    main()
        
        
def buy_snaks(inv):
    value = int(input('how many types of snaks do you want to buy?: '))
    if value < 0 or value > 6:
        print('Select range 1-5')
        main()
    else:
        for i in range(value):
            id_product = int(input('Enter Id Product do you want to buy?: '))
            if id_product in inv:
                product = inv[id_product]
                print(f'\tYour select Id: {id_product}, Name: {product['name']}, Price: S/.{product['price']}')
                name = product['name']
                price = product['price']
                quantity = int(input('Enter quantity: '))
                subtotal = price * quantity
                if quantity > product['quantity'] or quantity < 0:
                    print('error')
                    main()
                else:
                    # agregar compras a buy
                    buy[id_product]={
                        'name': name,
                        'price': price,
                        'quantity': quantity,
                        'subtotal': subtotal
                    }
                    # actualizar inventario
                    inv[id_product]['quantity'] = inv[id_product]['quantity']- quantity 
                print(f'added successfully: {name}')
                
    main()
    
    
def show_ticket(inv_buy):
    print('-' *80)
    print(f' Your Ticket:')
    if not inv_buy:
        print('Your cart is empty')
    else: 
        total = 0
        for id_product, detail in inv_buy.items():
            name = detail['name']
            price = detail['price']
            quantity = detail['quantity']
            subtotal = detail['subtotal']
            print(f'Id: {id_product}| {name} |P. Unitario: S/.{price} |C.: {quantity}| SubTotal = S/.{subtotal}')
            total += subtotal
        print(f'Total: S/.{total}')
    main()
# management system
def main():
    menu()
    option = int(input('Please Select your Option: '))
    if option == 1:
        show_snaks(inventory)
    elif option == 2:
        buy_snaks(inventory)
    elif option == 3:
        show_ticket(buy)
    elif option == 4:
        print('logging out of the sistems')
        exit()
    else:
        print('Try again')
    
menu()
main()