print('Calculator Application')
def menu():
    print('Menu:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
menu()

while True:
    value = int(input('Select an option: '))
    if value == 1:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = num1 + num2
        print(f'The result is: {result}')
        menu()
    elif value == 2:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = num1 - num2
        print(f'The result is: {result}')
        menu()
    elif value == 3:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = num1 * num2
        print(f'The result is: {result}')
        menu()
    elif value == 4:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        if num2 == 0:
            print('Error! Division by zero.')
            continue
        else:
            result = num1 / num2
            print(f'The result is: {result}')
            menu()
    elif value == 5:
        print('Exit...')
        break
    else:
        print('Invalid option, try again...')