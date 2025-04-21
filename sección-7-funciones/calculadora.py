def menu():
    print('Simple Calulator:')
    print('|1. ➕ Adition | 2. ➖ Subtraction| 3. ✖️  Multiplication| 4. ➗ Division | ❌ 5. Exit')
    print('-'*85)
    
def suma(a, b):
    result = a + b
    print(f'\tThe Result of {a} + {b} = {result}')
    main()
def resta(a, b):
    result = a - b
    print(f'\tThe Result of {a} - {b} = {result}')
    main()
def multi(a, b):
    result = a * b
    print(f'\tThe Result of {a} x {b} = {result}')
    main()
def divi(a, b):
    result = a / b
    print(f'\tThe Result of {a} / {b} = {result}')
    main()
    
def main():
    menu()
    values = [1,2,3,4,5]
    option = int(input('Select one option: '))
    if option not in values:
        print('Escoje las opciones que ves en el menu: ')
        main()
    elif option == 1:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        suma(a, b)
    elif option == 2:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        resta(a, b)
    elif option == 3:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        multi(a, b)
    elif option == 4:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        divi(a, b)
    elif option == 5:
        exit()
main()