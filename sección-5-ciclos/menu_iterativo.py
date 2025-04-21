espacio = 4
print('Sistem of administrator')
def menu():
    print('Menu:')
    print(" "* espacio, '1. Add user')
    print(" "* espacio, '2. Delete user')
    print(" "* espacio, '3. exit')

menu()

while True:
    value = int(input('Select an option: '))
    if value == 1:
        print('Add user...')
        menu()
    elif value == 2:
        print('Delete user...')
        menu()
    elif value == 3:
        print('Exit...')
        break
    else:
        print('Invalid option, try again...')