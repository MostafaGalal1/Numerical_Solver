from factories.abstract_method import AbstractMethod
import math


class FixedPoint(AbstractMethod):
    def __init__(self, function, x_initial, epsilon, iterations, service):
        self.function = function  # should be string (g(x)) the string of function should be like " x**2 + math.sin(x) "
        self.x_initial = x_initial    # should be float
        self.epsilon = epsilon    # should be float
        self.max_iteration = iterations    # should be float
        self.service = service

    def execute(self):
        try:
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
                if x_new != 0:
                    relative_error = self.service.apply_precision(abs((x_new - x_old) / x_new))
                    steps += "relative_error = " + str(relative_error) + "\n"
                else:
                    steps += "relative_error = ----" + "\n"
                steps += "________________________________\n"
                if relative_error <= self.epsilon:   # epsilon is the number of digits
                    steps += "\n" + "the root of f(x) = " + str(x_new) + "\n"
                    return steps
                x_old = x_new

        except ZeroDivisionError:
            return "There is no solution"

        except OverflowError:
            return "Diverges!"

        steps += "\n" + "the root of f(x) = " + str(x_new) + "\n"
        return steps