# VIP discounts

member = input("Are you a VIP member? (yes/no): ").strip().lower() #strip remueve espacios en blanco y lower convierte a minusculas
articles =  int(input("How many articles did you buy today? "))

discount = (member == "yes" and articles >= 10)

print(f'You have discount: {discount}')