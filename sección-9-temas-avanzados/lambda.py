from functools import reduce
# lambda es una funcion anónima pero muy util
# sirve para hacer funciones simples

suma = lambda x, y: x + y
print(suma(10, 20))

cuadrado = lambda x: x**2
print(cuadrado(10))

# se puede usar lambda para filtrar listas
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)

lista = [numbers for numbers in numbers if numbers % 2 ==0]
print(lista)
# se puede usar lambda para mapear listas
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(map(lambda x: x**2, numbers))
print(numbers)

lista2 = [numbers**2 for numbers in numbers]
print(lista2)

# reduce y map
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


result = reduce(lambda x, y: x + y, list_numbers)    
print(result)

suma_numeros = 0
for i in list_numbers:
    suma_numeros += i
print(suma_numeros)

suma2 = 0
for i in range(len(list_numbers)):
    suma2 += list_numbers[i]
print(suma2)    
    

