from symtable import *
from sympy import *
import math

def evaluation(equation, x):
    return eval(equation)


f = lambda x: eval("sin(x)")
x = Symbol('x')
dif = str(Derivative(eval("sin(x)"), x).doit())
y=lambda x: eval(dif.replace("cos","math.cos"))
print(None.replace("x",""))