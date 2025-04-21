# creamos un diccionario con los productos y sus precios
market = {'arroz': 15, 'azucar': 5, 'sal': 1, 'aceite': 10, 'leche': 7, 'huevo': 5, 'pan': 15}
# listamos los productos y sus precios
print('list to products')
for product in market:
    print(f'{product} -> {market[product]}')
# pedimos al usuario que ingrese la cantidad de productos que desea comprar
amount = int(input('how many products do you want to buy? '))
products = [] # iniciamos con una cesta vacia de productos
# pedimos al usuario que ingrese los productos que desea comprar
for i in range(amount):
    product = input('product: ').strip().lower()
    if product in market:
        products.append(product)
    else:
        print(f'{product} not found')
# funcion suma que recibe la cesta de productos y devuelve el total
def sum(cesta):
    subtotal = 0
    for product in cesta:
        subtotal += market[product]
    if subtotal > 5:
        total = (subtotal * 0.18) + subtotal
    else:
        total = subtotal
    return total
print('IGV: 18%')
for product in products:
    print(f'{product} -> S/.{market[product]}')
print(f'Total: {sum(products)}')



