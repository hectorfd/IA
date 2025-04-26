# leer archivos con python
name = 'mi_archivo.txt'

with open(name, 'r') as archivo:# r es para abrir el archivo en modo lectura
    contenido = archivo.read()# read es para leer el archivo
    #uso de readlines()
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())
    #print(contenido)
    
