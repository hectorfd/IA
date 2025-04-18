espacio = 4
print('Sistem of administrator')
print('Menu:')
print(" "* espacio, '1. Add user')
print(" "* espacio, '2. Delete user')
print(" "* espacio, '3. exit')

while True:
    value = int(input('Select an option: '))
    if value == 1:
        print('Add user...')
    elif value == 2:
        print('Delete user...')
    elif value == 3:
        print('Exit...')
        break
    else:
        print('Invalid option, try again...')