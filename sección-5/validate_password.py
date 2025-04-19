print('Login')

while True:
    password = input('Enter your password: ')
    if len(password)<6:
        print('Password must be at least 6 characters long.')
        continue
    else:
        print('Password is valid.')
        break