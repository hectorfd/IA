espacio = 40
print('Contact List')
def menu():
    print('Menu:')
    print('|1.✍️  Add contact','|2.⛔ delete contact |3. 🆎 view contacts| 4.Exit ❌|')
    print('-' * espacio,)
menu()
contact_list = {
    }

def management():
    option = int(input('Select an option: '))
    if option == 1:
        name = input('Enter the name:')
        if name in contact_list:
            print('⚠️ Contact already exists, try again...')
            management()
        else:
            print('Add contact...')
            phone = input('Enter the phone number:')
            email = input('Enter the email:')
            address = input('Enter the address:')
            contact_list[name] = {
                'telefono': phone,
                'email': email,
                'address': address
            }
            print(f'✅ Contact {name} added successfully')
            print('-' * espacio,)
            menu()
            management()
    elif option == 2:
        name = input('Enter the name of the contact to delete:')
        if name not in contact_list:
            print('⚠️ Contact not found, try again...')
            management()
        else:
            print(f'✅ Contact {name} deleted successfully')
            del contact_list[name]
            menu()
            management()
    elif option == 3:
        print('View contacts...')
        print('-' * espacio,)
        for name, info in contact_list.items():
            print(f'Name: {name}')
            print(f'Telephone: {info["telefono"]}')
            print(f'Email: {info["email"]}')
            print(f'Address: {info["address"]}')
            print('-' * espacio,)
        menu()
        management()
    elif option == 4:
        print('Exit...')
        print('-' * espacio,)
        print('Contact list:')
        print('-' * espacio,)
        for name, info in contact_list.items():
            print(f'Name: {name}')
            print(f'Telephone: {info["telefono"]}')
            print(f'Email: {info["email"]}')
            print(f'Address: {info["address"]}')
            print('-' * espacio,)
        exit()

management()