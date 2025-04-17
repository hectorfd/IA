AD = [18, 19, 20]
A = [14, 15, 16, 17]
B = [11,12,13]
C = [0,1,2,3,4,5,6,7,8,9,10]

grade = int(input('Enter your grade (0-20): '))

if grade in AD:
    print('Excellent')
elif grade in A:
    print('Good')
elif grade in B:
    print('Regular')
elif grade in C:
    print('Fail')
else:
    print('Invalid grade')