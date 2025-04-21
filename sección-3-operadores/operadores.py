# arithmetic operators
a = 10
b = 20
print(a + b)  # addition = 30
print(a - b)  # subtraction = -10
print(a * b)  # multiplication = 200
print(a / b)  # division = 0.5
print(a % b)  # modulus = 10
print(a ** b)  # exponentiation = 100000000000000000000
print(a // b)  # floor division = 0
# comparison operators
a = 10
b = 20
print(a == b)  # equal to = False
print(a != b)  # not equal to = True
print(a > b)  # greater than = False
print(a < b)  # less than = True
print(a >= b)  # greater than or equal to = False
print(a <= b)  # less than or equal to = True
# assignment operators
a = 10
b = 20
a += b  # a = a + b
print(a)
a -= b  # a = a - b
print(a)
a *= b  # a = a * b
print(a)
a /= b  # a = a / b
print(a)
a %= b  # a = a % b
print(a)
a **= b  # a = a ** b
print(a)
a //= b  # a = a // b
print(a)

# logical operators
a = True
b = False
print(a and b)  # logical AND = False
print(a or b)  # logical OR = True
print(not a)  # logical NOT = False
# identity operators
a = [1, 2, 3]
b = a
c = a.copy() # copy hace una copia superficial de la lista
print(a is b)  # True, is se usa para comparar la identidad de los objetos
print(a is not b)  # False, is not se usa para comparar la identidad de los objetos
print(a is c)  # False, porque c es una copia superficial de a
print(a is not c)  # True, porque c es una copia superficial de a
# membership operators
a = [1, 2, 3]
b = 1
print(b in a)  # True, in se usa para comprobar si un elemento está en una colección
print(b not in a)  # False 
# bitwise operators
a = 10
b = 20
# & este es el operador AND, | este es el operador OR, ^ este es el operador XOR
# ~ este es el operador NOT, << este es el operador de desplazamiento a la izquierda, >> este es el operador de desplazamiento a la derecha
#tabla de verdad en binario 1 & 1 = 1, 1 & 0 = 0, 1 | 0 basta que uno sea 1 para que el resultado sea 1
# cuando 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0
print(a & b)  # bitwise AND = 0, porque en binario  10:  01010 and 20: 10100  = 00000
print(a | b)  # bitwise OR = 30, porque en binario  10:  01010 or 20: 10100  = 11110
print(a ^ b)  # bitwise XOR = 30, porque en binario  10:  01010 xor 20: 10100  = 11110
print(~a)  # bitwise NOT = -11, porque en binario  10:  01010 not = 10101
print(a << 2)  # left shift = 40, porque en binario  10:  01010 << 2 = 101000
print(a >> 2)  # right shift = 2, porque en binario  10:  01010 >> 2 = 00010
# ternary operator
a = 10
b = 20
# c es igual a a si a es mayor que b, de lo contrario c es igual a b
c = a if a > b else b# primero se pone a luego if porque es el valor que se va a devolver si la condicion es verdadera
print(c)  # 20
# null coalescing operator
a = None
b = 20
c = a if a is not None else b
print(c)  # 20
# walrus operator
a = 10
# esto : es un operador de asignación, se usa para asignar un valor a una variable y luego usar esa variable en una expresión
# en este caso se asigna el valor de a a n y luego se compara si n es mayor que 5
# si n es mayor que 5 se imprime n
if (n := a) > 5: # antes tenias que hacer esto n=10 si n> 5 print(n) pero ahora puedes hacer esto := asigna en la misma linea
    print(n)  # 10
    
if (joder := a) > 5:
    print(joder)  # 10
# f-string operator
a = 10
b = 20
c = f'The sum of {a} and {b} is {a + b}'
print(c)  # The sum of 10 and 20 is 30
# formatted string operator
a = 10
b = 20
c = 'The sum of {} and {} is {}'.format(a, b, a + b)
print(c)  # The sum of 10 and 20 is 30
# string concatenation operator
a = 'Hello'
b = 'World'
c = a + ' ' + b
print(c)  # Hello World
# string repetition operator
a = 'Hello'
b = 3
c = a * b
print(c)  # HelloHelloHello
# string slicing operator
a = 'Hello World'
b = a[0:5]
print(b)  # Hello
# string indexing operator
a = 'Hello World'
b = a[0]
print(b)  # H
# string length operator
a = 'Hello World'
b = len(a)
print(b)  # 11
# string membership operator
a = 'Hello World'
b = 'Hello' in a
print(b)  # True
# string formatting operator
a = 'Hello'
b = 'World'
c = '{} {}'.format(a, b)
print(c)  # Hello World
# string interpolation operator
a = 'Hello'
b = 'World'
c = f'{a} {b}'
print(c)  # Hello World
# string split operator
a = 'Hello World'
b = a.split(' ')
print(b)  # ['Hello', 'World']
# string join operator
a = ['Hello', 'World']
b = ' '.join(a)
print(b)  # Hello World
# string replace operator
a = 'Hello World'
b = a.replace('World', 'Python')
print(b)  # Hello Python
# string upper operator
a = 'Hello World'
b = a.upper()
print(b)  # HELLO WORLD
# string lower operator
a = 'Hello World'
b = a.lower()
print(b)  # hello world
# string title operator
a = 'hello world'
b = a.title()
print(b)  # Hello World
# string capitalize operator
a = 'hello world'
b = a.capitalize()
print(b)  # Hello world
# string strip operator
a = '   Hello World   '
b = a.strip()
print(b)  # Hello World
# string lstrip operator
a = '   Hello World   '
b = a.lstrip()
print(b)  # Hello World
# string rstrip operator
a = '   Hello World   '
b = a.rstrip()
print(b)  #    Hello World
# string find operator
a = 'Hello World'
b = a.find('World')
print(b)  # 6
# string rfind operator
a = 'Hello World'
b = a.rfind('World')
print(b)  # 6
# string index operator
a = 'Hello World'
b = a.index('World')
print(b)  # 6
# string rindex operator
a = 'Hello World'
b = a.rindex('World')
print(b)  # 6
# string count operator
a = 'Hello World'
b = a.count('o')
print(b)  # 2
# string startswith operator
a = 'Hello World'
b = a.startswith('Hello')
print(b)  # True
# string endswith operator
a = 'Hello World'
b = a.endswith('World')
print(b)  # True