# Lend books

student = input('do you student? (yes/no): ').strip().lower()
distance = float(input('how far do you live from the library? (km): '))

lend = (student == 'yes' or distance <= 3)

print(f'You can lend books: {lend}')