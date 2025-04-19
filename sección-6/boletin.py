espacio = 60
print('subscriptor boletin')
boletin = set({'juan@gmail.com', 'pedro@gmail.com'})
def menu():
    list = ['|1. Subscribe|', '2. Unsubscribe|', '3. Exit|', '4. List subscribers|']
    print('Menu:')
    for i in list:
        print(i, end =' ')
    print('\n')
    print('-' * espacio,)
menu()

while True:
    option = int(input('select an option: '))
    if option == 1:
        value = int(input('Enter the number of subscribers: '))
        if value <=0:
            print('Invalid number, try again...')
            menu()
            continue
        else:
            for i in range(value):
                email = input(f'Enter email {i + 1}: ')
                if email in boletin:
                    print('⚠️ Email already axists, try again...')
                    continue
                else:
                    print(f'✅ Email {email} added to the list')
                    print('-' * espacio,)
                    boletin.add(email)
            menu()
    elif option == 2:
        email = input('Enter the email to unsubscribe: ')
        if email not in boletin:
            print('Email not found, try again... ⚠️')
            menu()
            continue
        else:
            print(f'✅ Email {email} removed from the list')
            boletin.remove(email)
            menu()
    elif option == 3:
        print('Exit...')
        break
    elif option == 4:
        print('List of subscribers:')
        print('-' * espacio,)
        c = 1
        for email in boletin:
            print(f'{c}.- {email}')
            c+=1
        print('-' * espacio,)
        menu()
    
        

        
    
    