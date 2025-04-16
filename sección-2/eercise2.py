# Email Generator

name = input('Enter your name:')
last_name = input('Enter your last name:')

email = f"{name.lower()}.{last_name.lower()}@gmail.com"

print(f"Your email is: {email}")