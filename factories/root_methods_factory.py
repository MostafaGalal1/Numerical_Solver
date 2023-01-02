from open_methods.Bisection import *
from open_methods.FalsePosition import *
from open_methods.FixedPoint import *
from open_methods.NewtonRaphson import *
from open_methods.Secant import *


class RootsFactory:
   def __init__(self, method, service, function, epsilon = 0.00001, iterations = 50, x_upper=None, x_lower=None, x_initial=None, derivative=""):
        self.method = method.lower()
        self.service = service
        self.function = function.replace("cos","math.cos").replace("sin","math.sin").replace("exp","math.exp")  # should be string   the string of function should be like " x**2 + math.sin(x) "
        self.derivative = derivative.replace("cos","math.cos").replace("sin","math.sin").replace("exp","math.exp")  # should be string   the string of function should be like " x**2 + math.sin(x) "
        self.x_upper = float(x_upper)    # should be float
        self.x_lower = float(x_lower)    # should be float
        self.x_initial = float(x_initial)    # should be float
        self.epsilon = pow(10, -epsilon)    # should be float
        self.max_iteration = iterations    # should be float

   def create(self):
       if self.method == "bisection":
            return Bisection(self.function, self.x_upper, self.x_lower, self.epsilon, self.max_iteration, self.service)
       elif self.method == "false-position":
            return FalsePosition(self.function, self.x_upper, self.x_lower, self.epsilon, self.max_iteration, self.service)
       elif self.method == "fixed point":
            return FixedPoint(self.function, self.x_initial, self.epsilon, self.max_iteration, self.service)
       elif self.method == "newton-raphson":
            return NewtonRaphson(self.function, self.x_initial, self.derivative, self.epsilon, self.max_iteration, self.service)
       elif self.method == "secant method":
            return Secant(self.function, self.x_upper, self.x_lower, self.epsilon, self.max_iteration, self.service)
