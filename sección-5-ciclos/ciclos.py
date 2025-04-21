# bucles or cicles
# for loop
for i in range(10): # i es el iterador y range es la función que genera una secuencia de números, 10 es el límite
    print(i)
# while loop
i = 0 # i es el iterador inicia en 0 porque es el primer número de la secuencia
while i < 10: # mientras i sea menor que 10
    print(i) # imprime el valor de i
    i += 1 # incrementa el valor de i en 1
# do while loop
i = 0
while True:# inicia un bucle infinito
    print(i)
    i += 1
    if i >= 10:# si i es mayor o igual a 10
        break #break es una instrucción que se utiliza para salir de un bucle 
# for loop with else
for i in range(10):
    print(i)
else:# for permite usar else cuando se termina el bucle sin usar break
    print('End of for loop')
# while loop with else
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('End of while loop')
# break statement
for i in range(10):
    if i == 5:
        break
    print(i)
# continue statement
for i in range(10):
    if i == 5:
        continue# continue es una instrucción que se utiliza para saltar a la siguiente iteración del bucle
    print(i)
# pass statement
for i in range(10):
    if i == 5:
        pass# pass es una instrucción que se utiliza como un marcador de posición, no hace nada
    print(i)
# nested loops
# sete tipo de bucles sirve para iterar sobre una secuencia de elementos, como una lista o un rango
for i in range(3):
    for j in range(3):
        print(i, j)
# list comprehension
squares = [i**2 for i in range(10)]# i**2 calcula el cuadrado de i, ejemplo i=0, despues i=1, i=2, i=3, i=4, i=5, i=6, i=7, i=8, i=9 
print(squares)# resultado = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# dictionary comprehension
squares_dict = {i: i**2 for i in range(10)} # i: i**2 crea un diccionario donde la clave es i y el valor es el cuadrado de i
print(squares_dict)# Resultado = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# list comprehension with if
squares_even = [i**2 for i in range(10) if i % 2 == 0]# aplica una condición para filtrar los números pares
print(squares_even)# resultado = [0, 4, 16, 36, 64]
# dictionary comprehension with if
squares_even_dict = {i: i**2 for i in range(10) if i % 2 == 0}
print(squares_even_dict)
