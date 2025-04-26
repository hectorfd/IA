# crear un archivo
name = 'mi_archivo.txt'

with open(name, 'w') as archivo:
    archivo.write('Hola mundo\n')
    archivo.write('asi se agrega nueva informacion al archivo desde with')


# mejorando el codigo arriba usaremos el metodo with
# archivo = open(name, 'w') # w sobrescribe cualquier cosa

# archivo.write('Hola mundo\n')
# archivo.write('asi se agrega informacion al archivo')

# archivo.close() # siempre es importante cerrar el archivo para evitar fugas de memoria

print('El archivo se ha creado ')