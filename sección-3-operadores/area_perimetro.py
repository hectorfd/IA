
altura = int(input('Ingrese la altura del rectangulo: '))
base = int(input('Ingrese la base del rectangulo: '))
area = altura * base
perimetro = (altura + base) * 2

print('+'+'-' * base + '+')# este es el techo
for _ in range(altura):# este es el cuerpo
    print('|' + ' ' * base + '|')# espacio entre las barras
print('+'+'-' * base + '+')# este es el suelo
print(f'Area: {area}')
print(f'Perimetro: {perimetro}')