price = float(input('Enter the total price of the items: '))
members = input('Are you a menber? (yes/no): ').strip().lower()
if price > 100 and members == 'yes':
    discount = 0.1
elif price > 100 and members == 'no':
    discount = 0.05
else:
    discount = 0
total = price - (price * discount)
print(f'The total price is: {total}')