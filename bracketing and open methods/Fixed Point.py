from methods.abstract_method import *
import math


class fixed_point(AbstractMethod):
    def __init__(self, function, x_intial, epsilon, iterations, service):
        self.function = function  # should be string (g(x)) the string of function should be like " x**2 + math.sin(x) "
        self.x_initial = x_intial    # should be float
        self.epsilon = epsilon    # should be float
        self.max_iteration = iterations    # should be float
        self.service = service

    def execute(self):
        g = lambda x: eval(self.function)  # this is the function
        relative_error = 0
        iteration = 0
        x_old = self.x_initial
        x_new = 0
        steps = ""
        while iteration < self.max_iteration:
            iteration += 1
            x_new = self.service.apply_precision(g(x_old))
            steps += "Iteration Number " + str(iteration) + ": \n"
            steps += "x_i = " + str(x_new) + " | x_i+1 = " + str(x_old) + "\n"
            try:
                relative_error = self.service.apply_precision(abs(x_new - x_old) / abs(x_new))
                steps = "Relative_error = " + str(relative_error * 100) + " % " + "\n"
            except ZeroDivisionError:
                steps = "Relative_error = ----" + "\n"
            steps += "________________________________\n"
            if abs(x_new - x_old) <= pow(10, -self.epsilon):   # epsilon is the number of digits
                steps += "\n" + "the root of f(x) = " + str(x_new) + "\n"
                return steps
