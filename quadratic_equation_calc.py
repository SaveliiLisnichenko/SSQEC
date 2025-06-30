import math
import sys

print("""
======================
Welcome to the Python Quadratic Equation Calc.
======================
You will need to input 3 integers for variables a, b, and c from a valid quadratic equation in this format:
ax^2 + bx + c = 0
""")

a = 0
b = 0
c = 0

try:
    a = int(input('Input for a: '))
except:
    print('input an integer dumbass')
    sys.exit()

try:
    b = int(input('Input for b: '))
except:
    print('input an integer dumbass')
    sys.exit()

try:
    c = int(input('Input for c: '))
except:
    print('input an integer dumbass')
    sys.exit()

print('This is what the equation looks like currently: \n' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c) + ' = 0')

try:
    solution1 = (-b + math.sqrt((math.pow(b, 2) - (4 * a * c))))/(2 * a)
    solution2 = (-b - math.sqrt((math.pow(b, 2) - (4 * a * c))))/(2 * a)
except ValueError:
    print('Gum-gum square root of a negative number!')
    sys.exit()

print('x = (' + str(solution1) + ', ' + str(solution2) + ')')
