espacio = 5
print('automated teller machine')
def menu():
    print('Menu:')
    print(" "* espacio, '1. Deposit')# deposito
    print(" "* espacio, '2. Withdraw')# retiro
    print(" "* espacio, '3. Check balance') # verificar saldo
    print(" "* espacio, '4. Exit')# salir
menu()
mount = 0
while True:
    value = int(input('Select an option: '))
    if value == 1:
        deposit = float(input('Enter the amount to deposit: '))
        if deposit <= 0:
            print('Invalid amount, try again...')
            continue
        else:
            print(f'Deposited: {deposit}')
        print('Deposit...')
        mount += deposit
        print(f'New balance: {mount}')
        menu()
    elif value == 2:
        withdraw = float(input('Enter the amount to withdraw: '))
        if withdraw <= 0:
            print('Invalid amount, try again...')
            continue
        elif withdraw > mount:
            print('Insufficient funds, try again...')
            continue
        else:
            print(f'Withdrawn: {withdraw}')
        mount -= withdraw
        print('Withdraw...')
        print(f'New balance: {mount}')
        
        menu()
    elif value == 3:
        print('Check balance...')
        print(f'Balance: {mount}')
        menu()
    elif value == 4:
        print('Exit...')
        break
    else:
        print('Invalid option, try again...')