import random
print('Riddles')
riddles = random.randint(1, 50)
count = 0
clue = ' '
while True:
    number = int(input('Enter a number: '))
    if number != riddles:
        print('Try again...')
        count += 1
        clue = 'To low ➡️' if number < riddles else 'To high ⬅️'
        print(clue)
    else:
        print('Congratulations! You guessed the number.')
        print(f'You took {count} attempts.')
        break