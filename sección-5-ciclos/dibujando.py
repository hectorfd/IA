print('draw simetric')
rows = int(input('Enter the number of rows: '))
# 1, 3, 5, 7, 9, 11, 13, 15
for i in range(rows):
    spaces = ' ' * (rows - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

# i = 0 in range(rows = 3)
# spaces = ' ' * (3 - 0 - 1)
# stars = '*' * (2 * 0 + 1)
#   *
# i = 1 in range(rows = 3)
# spaces = ' ' * (3 - 1 - 1)
# stars = '*' * (2 * 1 + 1)
#  ***
# i = 2 in range(rows = 3)
# spaces = ' ' * (3 - 2 - 1)
# stars = '*' * (2 * 2 + 1)
# *****

