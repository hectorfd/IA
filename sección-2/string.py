name = 'Hector Ferro Dávalos'
age = 31

mensajes = 'Hi, my name is ' + name + ' and I am ' + str(age) + ' years old'
print(mensajes)
# f-string
mensajes = f"Hi, my name is {name} I'm {age} years old"
print(mensajes)
# f-string con formato
mensajes = f'Hi, my name is {name} I am {age:02} years old' # rellena con ceros a la izquierda
print(mensajes)
# f-string con formato y expresiones
mensajes = f'This year I turn {age + 1} years old'
print(mensajes)

#! large strings
mensaje = 'Mi name is Hector Ferro I am 31 years old'
print(mensaje)

#! functions strings
# upper
mensaje = mensaje.upper()
print(mensaje)
# lower
mensaje = mensaje.lower()
print(mensaje)
# title
mensaje = mensaje.title()
print(mensaje)
# capitalize
mensaje = mensaje.capitalize()
print(mensaje)
# strip
mensaje = mensaje.strip() # elimina espacios en blanco al principio y al final
print(mensaje)
# lstrip
mensaje = mensaje.lstrip() # elimina espacios en blanco al principio
print(mensaje)
# rstrip
mensaje = mensaje.rstrip() # elimina espacios en blanco al final
print(mensaje)
# split
mensaje = mensaje.split() # separa el string en una lista de palabras
print(mensaje)
# join
mensaje = ' '.join(mensaje) # une la lista de palabras en un string
print(mensaje)
# find
mensaje = mensaje.find('Hector') # busca la posicion de la palabra Hector
print(mensaje)


mensaje2 = 'Hector Ferro Dávalos'
# index
mensaje = mensaje2.index('Hector') # busca la posicion de la palabra Hector
# replace
mensaje = mensaje2.replace('Hector', 'Héctor') # reemplaza la palabra Hector por Héctor
print(mensaje)
# len
mensaje = len(mensaje2) # devuelve la longitud del string
print(mensaje)
# count
mensaje = mensaje2.count('Hector') # cuenta cuantas veces aparece la palabra Hector
print(mensaje)
# startswith
mensaje = mensaje2.startswith('Hector') # devuelve True si el string empieza con Hector
print(mensaje)
# endswith
mensaje = mensaje2.endswith('Hector') # devuelve True si el string termina con Hector
print(mensaje)
# isalpha
mensaje = mensaje2.isalpha() # devuelve True si el string solo contiene letras
print(mensaje)