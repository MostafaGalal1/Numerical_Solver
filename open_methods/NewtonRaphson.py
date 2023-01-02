from factories.abstract_method import AbstractMethod
import math


class NewtonRaphson(AbstractMethod):
    def __init__(self, function, x_initial, derivative, epsilon, iterations, service):
        self.function = function  # should be string (g(x)) the string of function should be like " x**2 + math.sin(x) "
        self.x_initial = x_initial    # should be float
        self.derivative = derivative
        self.epsilon = epsilon    # should be float
        self.max_iteration = iterations    # should be float
        self.service = service

    def execute(self):
        try:
            f = lambda x: eval(self.function)
            dif = lambda x: eval(self.derivative)
            x0 = self.x_initial
            count = 1
            steps = ""
            while True:
                x1 = self.service.apply_precision(x0 - f(x0) / dif(x0))
                steps += "Iteration Number " + str(count) + ": \n"
                steps += "xi = " + str(x1) + " | f(xi) = " + str(self.service.apply_precision(f(x1))) +"\n"
                steps += "f'(xi) = " + str(self.service.apply_precision(dif(x1))) + " | relative_error = " + str(self.service.apply_precision(abs(x1-x0)/x1)) +"\n"
                steps += "________________________________\n"
                if (x1 != 0 and self.service.apply_precision(abs(x1 - x0)/x1) < self.epsilon) or (count >= self.max_iteration):
                    break
                x0 = x1
                count += 1
            steps += "\n" + "the root of f(x) = " + str(x0) + "\n"
            return steps

        except ZeroDivisionError:
            return "There is no solution"

        except OverflowError:
            return "Diverges!"