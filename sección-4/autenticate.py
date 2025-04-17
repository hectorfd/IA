user = 'hector'
password = '1234'

def login():
    user_input = input('Enter your username:')
    password_input = input('Enter your password:')
    if user_input == user and password_input == password:
        print('welcome to the system')
    elif user_input != user and password_input == password:
        print('User not autenticate')
        login()
    elif user_input == user and password_input != password:
        print('Password not autenticate')
        login()
    elif user_input != user and password_input != password:
        print('User and password not autenticate')
        login()
    else:
        print('User not autenticate')
        login()
        
login()