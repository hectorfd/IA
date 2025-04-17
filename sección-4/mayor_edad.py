MAYOR = 18

age = int(input('Ingrese su edad: '))
mayor = age >= MAYOR

if mayor:
    print('Es mayor de edad')
else:
    print('Es menor de edad')