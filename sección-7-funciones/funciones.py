# Funciones
# simples sin parametros
def saludar():
    print("Hola, ¿cómo estás?")
# simples con parametros
def saludar_persona(nombre):
    print(f"Hola, {nombre}, ¿cómo estás?")
# funciones con retorno
def sumar(a, b):
    return a + b
# funciones con retorno y parametros
def sumar_con_mensaje(a, b):
    resultado = a + b
    return f"La suma de {a} y {b} es {resultado}"

# funciones con argumentos por nombre
def create_person(name, last_name='', age=0):
    print (f'Nombre: {name}, Apellido: {last_name}, Edad: {age}')

create_person(name='Juan', last_name='Pérez', age=30)

# regresar una tupla de valores desde una funcion
def persona_mayuscula(nombre, apellido, edad):
    return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad = persona_mayuscula('Juan', 'Pérez', 30)
print(f'Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}')

# funciones con argumentos variables

def super_con_poderes(name, *args):
    print(f'superhero: {name} - {args}')
    for i in args:
        print(f'\tsuperpoder: {i}')# \t = es un caracter de escape forma una tabulación
    
super_con_poderes('Spiderman', 'Teleraña', 'Instinto aracnido')
super_con_poderes('Thor', 'Trueno', 'Martillo', 'Fuerza')

# funciones con argumentos varibles diccionarios

def person(name, *args, **kwargs):
    print(f'Nombre: {name}')
    for i in args:
        print(f'\tHabilidades: {i}')
    for j in kwargs:
        print(f'\tDatos Personales: {j}')
person('Hector', 'Programación', 'Ciencia de Datos', edad = 32, direccion = 'tamburco', email = 'hector@gmail.com' )

# funciones de tipo clave valor

def imprimir(**kwargs):
    print('Valores recibidos')
    for llave, valor in kwargs.items():
        print(f'\t{llave} : {valor}')
        
imprimir(nombre = 'Hector', edad = 31, ciudad = 'Abancay')