print('Factorial of a number')
#* 4! = 4*(4-1)*(4-2)*(4-3) -> 4! = 4*3*2*1 = 24

def cal_factorial(number):
    factorial = number
    for i in range(1, number):
        factorial *= (number - i)
    print(f'factorial of {number} is: {factorial}')
# factorial = 4
# first iteration
# i = 1 
# factorial = 4 * (4-1) = 12
# second iteration
# i = 2
# factorial = 12 * (4-2) = 24
# thirt iteration
# i = 3
# factorial = 24 * (4-3) = 24
# cuarter iteration
# i = 4 -> number = 4 -> i = number -> end

cal_factorial(4)