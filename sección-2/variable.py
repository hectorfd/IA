number = 5
name = 'Hector'
list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)
dict = {'name': 'Hector', 'age': 31}
set = {1, 2, 3, 4, 5} 
bool = True
float = 5.5
complex = 5 + 3j

print(f'Code: {number}\nName: {name} \nEdad: {dict['age']} ' )


#! Reglas

# 1. No se puede empezar con un número
var = 1 # 2=5 dara un error
# 2. No se pueden usar caracteres especiales
#$$## = 5 -> # el numeral es un caracter especial
# 3. No se pueden usar espacios
# my var = 5 -> # el espacio es un caracter especial
# 4. No se pueden usar palabras reservadas
#del = 5 # del es una palabra reservada
# 5. para constantes se recomienda usar mayusculas
PI = 3.141516
# 6. Se recomienda usar snake_case para variables y funciones
full_name_please = 'Hector Ferro Davalos'
# 7. Se recomienda usar PascalCase para clases
class Person:
    pass
