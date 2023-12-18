import sympy as sp
import math

expression_str = input("Please enter a function f(x): ")
expression = sp.sympify(expression_str)

x = sp.symbols('x')

n = int(input("Enter the number of how many step should calculate: "))
c = int(input("write number for c or x0: "))
a = 1
pasuxi = expression.subs(x,c)
simbolo = sp.symbols('x')
try:
    derivatives = {}

    for order in range(1, n + 1):
        derivative = sp.diff(expression, x, order)
        simplified_derivative = sp.simplify(derivative)
        derivatives[f'd{order}'] = simplified_derivative

    for i in range(1,n+1):
        key = f'd{i}'
        if key in derivatives:
            functcia = derivatives[key]
        factorial = math.factorial(a)
        functcia1 = sp.sympify(functcia)
        gamotvlili = functcia1.subs(x,c)
        pasuxi = pasuxi + (gamotvlili*  (simbolo-c)**a)/factorial
        print(i,". ", pasuxi)
        a=a+1

except sp.SympifyError:
    print("Invalid input. Please enter a valid mathematical expression.")

hello=input("")





