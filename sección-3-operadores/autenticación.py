user = 'hector'
password = '1234'
def login():
    user_input = input('Enter your username:')
    password_input = input('Enter your password:')
    if user_input == user and password_input == password:
        print('User autenticate successfully')
    else:
        print('User not autenticate')
        login()
login()