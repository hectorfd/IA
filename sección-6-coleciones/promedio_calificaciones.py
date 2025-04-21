print('grade average')

def grade_average():
    grades = []
    while True:
        number = int(input('Enter the number of grades: '))
        if number <= 0:
            print('numbers must be greater than 0')
            continue
        elif number > 0:
            break
    for i in range(number):
        grade = float(input(f'Enter the grade {i + 1}: '))
        if grade < 0 or grade > 20:
            print('The grade must be between 0 and 20')
            continue
        grades.append(grade)
    average = sum(grades) / len(grades)
    print(f'The average is: {average}')

grade_average()