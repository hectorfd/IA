products = [
    ('P001', 'LECHE', 1.50),
    ('P002', 'HUEVO', 0.50),
    ('P003', 'AZUCAR', 0.75),
    ('P004', 'ACEITE', 2.00),
    ('P005', 'SAL', 0.25),
    ('P006', 'ARROZ', 1.00),
    ('P007', 'FIDEOS', 1.20),
    ('P008', 'CARNE', 5.00),
    ('P009', 'VERDURA', 2.50),
    ('P010', 'FRUTA', 3.00)
]
    
def sum():
    total = 0
    for i in products:
        id, description, price = i
        print(f'ID: {id}, Description: {description}, Price: {price}')
        total += price
    return total
print(f'Total: {sum()}')