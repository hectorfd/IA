#anexar informacion
name = 'mi_archivo.txt'

with open(name, 'a') as archivo: # a es para anexar informacion
    archivo.write('asi se agrega nueva informacion al archivo desde with')
    
print(f'El archivo se ha modificado: {name}')