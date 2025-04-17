invierno = [1,2,12]
primavera = [3,4,5]
verano = [6,7,8]
otoño = [9,10,11]
value = int(input('Enter month (1-12): '))

if value in invierno:
    print('Invierno')
elif value in primavera:
    print('Primavera')
elif value in verano:
    print('Verano')
elif value in otoño:
    print('Otoño')
else:
    print('Invalid month')
