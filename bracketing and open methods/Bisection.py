from factories.abstract_method import AbstractMethod
import math


class Bisection(AbstractMethod):
    def __init__(self, function, x_upper, x_lower, epsilon, iterations, service):
        self.function = function  # should be string   the string of function should be like " x**2 + math.sin(x) "
        self.x_upper = x_upper    # should be float
        self.x_lower = x_lower    # should be float
        self.epsilon = epsilon    # should be float
        self.max_iteration = iterations    # should be float
        self.service = service

    def execute(self):
        f = lambda x: eval(self.function)  # this is the function
        absolute_error = 0
        iteration = 0
        x_r_new = 0
        x_r_old = 0
        x_u = self.x_upper
        x_l = self.x_lower
        steps = ""
        if f(x_u) * f(x_l) > 0:
            steps = " Error "
            return steps
        while iteration < self.max_iteration:
            iteration += 1
            x_r_new = self.service.apply_precision((x_l + x_u) / 2)
            steps += "Iteration Number " + str(iteration) + ": \n"
            steps += "x_l = " + str(x_l) + " | x_u = " + str(x_u) + " | x_r = " + str(x_r_new) + "\n"
            steps += "f(x_l) = " + str(f(x_l)) + " | f(x_u) = " + str(f(x_u)) + " | f(x_r) = " + str(f(x_r_new)) + "\n"
            if iteration != 1:
                try:
                    absolute_error = self.service.apply_precision(abs(x_r_new - x_r_old))
                    steps = "absolute_error = " + str(absolute_error) + "\n"
                except ZeroDivisionError:
                    steps = "absolute_error = ----" + "\n"
            steps += "________________________________\n"
            if abs(x_r_new - x_r_old) <= pow(10, -self.epsilon):   # epsilon is the number of digits
                steps += "\n" + "the root of f(x) = " + str(x_r_new) + "\n"
                return steps
            elif f(x_r_new) * f(x_l) < 0:
                x_u = x_r_new
                x_r_old = x_r_new
            elif f(x_r_new) * f(x_u) < 0:
                x_l = x_r_new
                x_r_old = x_r_new
            elif f(x_r_new) == 0:
                return steps
            else:
                steps += "error"
                return steps
