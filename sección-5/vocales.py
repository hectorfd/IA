# Declarar la variable
cadena = ("Hola Mundo")
# Agregar el ciclo for
vocals = ["a", "e", "i", "o", "u"]
count = 0
for i in cadena.lower():
    if i in vocals:
        count += 1
# Imprimir la cantidad de vocales encontradas en la cadena
print(count)