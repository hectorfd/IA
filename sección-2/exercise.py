# code generator 

name = input('Enter your name:')
last_name = input('Enter your last name:')
year_of_birth = int(input('Enter your year of birth in format(yyyy)please:'))

#* function code generator
def generate_code(name, last_name, year_of_birth):
    #* code generator
    code = f"{name[:2].upper()}{last_name[:2].upper()}{str(year_of_birth)[:2]}"
    return code

# print
print(f"Your code is: {generate_code(name, last_name, year_of_birth)}") 