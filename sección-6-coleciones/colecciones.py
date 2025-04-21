# colecciones, listas, tuplas, conjuntos set, diccionarios, diccionarios anidados, rangos
# Listas
list = [1, 2, 3, 4, 5]
print(list)
# funciones de lista
list.append(6) # agregar un elemento al final de la lista
print(list) # [1, 2, 3, 4, 5, 6]
list.insert(0, 0) # agregar un elemento al inicio de la lista
print(list)# [0, 1, 2, 3, 4, 5, 6]
list.remove(3) # eliminar un elemento de la lista
print(list) # [0, 1, 2, 4, 5, 6]
list.pop() # eliminar el ultimo elemento de la lista
print(list) # [0, 1, 2, 4, 5]
list.sort() # ordenar la lista
print(list) # [0, 1, 2, 4, 5]
list.reverse() # invertir la lista
print(list) # [5, 4, 2, 1, 0]
list.clear() # limpiar la lista
print(list) # []
# del list # eliminar la lista
# del list[0] # eliminar el primer elemento de la lista
# Listas anidadas
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# tuplas
tuple = (1, 2, 3, 4, 5)
print(tuple) # (1, 2, 3, 4, 5)
# funciones de tupla
# tuple.append(6) # agregar un elemento al final de la tupla
# print(tuple) # (1, 2, 3, 4, 5, 6)
# tuple.insert(0, 0) # agregar un elemento al inicio de la tupla
# print(tuple) # (0, 1, 2, 3, 4, 5)
# tuple.remove(3) # eliminar un elemento de la tupla
# print(tuple) # (0, 1, 2, 4, 5)
# tuple.pop() # eliminar el ultimo elemento de la tupla
# conjuntos set
set = {1, 2, 3, 4, 5}
print(set)
# funciones de set
set.add(6) # agregar un elemento al final del set
print(set) # {1, 2, 3, 4, 5, 6}
set.remove(3) # eliminar un elemento del set
print(set) # {1, 2, 4, 5, 6}
set.discard(3) # eliminar un elemento del set
print(set) # {1, 2, 4, 5, 6}
set.pop() # eliminar el primer elemento del set
print(set) # {2, 4, 5, 6}
set.clear() # limpiar el set
print(set) # set()
# del set # eliminar el set
# del set[0] # eliminar el primer elemento del set
# diccionarios
dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(dict)
# funciones de diccionario
dict['name'] = 'Jane' # cambiar el valor de un elemento del diccionario
print(dict) # {'name': 'Jane', 'age': 30, 'city': 'New York'}
dict['country'] = 'USA' # agregar un elemento al diccionario
print(dict) # {'name': 'Jane', 'age': 30, 'city': 'New York', 'country': 'USA'}
dict.pop('age') # eliminar un elemento del diccionario
print(dict) # {'name': 'Jane', 'city': 'New York', 'country': 'USA'}
dict.clear() # limpiar el diccionario
print(dict) # {}
# del dict # eliminar el diccionario
# diccionarios anidados
dict = {'name': 'John', 'age': 30, 'city': 'New York', 'address': {'street': '5th Ave', 'number': 10}}
print(dict)
# rangos
#range = range(1, 10)
#print(range)
# funciones de rango
# funciones de rango
# range(1, 10, 2) # rango de 1 a 10 con paso de 2
# print(list(range)) # [1, 3, 5, 7, 9]
# range(10, 1, -1) # rango de 10 a 1
# print(list(range)) # [10, 9, 8, 7, 6, 5, 4, 3, 2]
# range(1, 10, -1) # rango de 1 a 10 con paso de -1
# print(list(range)) # [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
#ran = range(1, 10, 2)  # rango de 1 a 10 con paso de 2
#print(list(ran))       