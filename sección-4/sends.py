weight = float(input('Enter your weight in kg: '))
destination = input('Enter if your package is going to a Nacional or Internacional destination: ').strip().lower()
cost = 0
if destination == 'nacional':
    cost = weight * 10
elif destination == 'internacional':
    cost = weight * 20
else:
    print('Invalid destination')
    exit()
print(f'The cost of sending the package is: S/.{cost}')