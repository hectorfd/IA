print("funcion zip")
# se usa para unir dos listas
names = ['Hector', 'Javier', 'Alex']
ages = [31, 32, 33]
cities = ['Cusco', 'Lima', 'Arequipa']

# unir las listas

list_zip = zip(names, ages, cities)

# para mostrar el zip se debe iterar
# el resultado es una tupla
for person in list_zip:
    print(person)
