from factories.abstract_method import AbstractMethod

class Secant(AbstractMethod):
    def __init__(self, function, x_upper, x_lower, epsilon, iterations, service):
        self.function = function  # should be string   the string of function should be like " x**2 + math.sin(x) "
        self.x_upper = x_upper    # should be float
        self.x_lower = x_lower    # should be float
        self.epsilon = epsilon    # should be float
        self.max_iteration = iterations    # should be float
        self.service = service

    def execute(self):
        try:
            count = 1
            f = lambda x: eval(self.function)
            x0 = self.x_lower
            x1 = self.x_upper
            steps = ""
            while True:
                x2 = self.service.apply_precision(x1 - self.service.apply_precision(f(x1) * (x1 - x0) / self.service.apply_precision(f(x1) - f(x0))))
                steps += "Iteration Number " + str(count) + ": \n"
                steps += "Xi-1 = " + str(x0) + " | Xi = " + str(x1) + "\n"
                steps += "f(Xi-1) = " + str(self.service.apply_precision(f(x0))) + " | f(Xi) = " + str(self.service.apply_precision(f(x1))) + "\n"
                steps += "relative_error = " + str(self.service.apply_precision(abs(x1-x0)/x1)) + "\n"
                steps += "________________________________\n"
                if (x2 != 0 and self.service.apply_precision(abs(x2 - x1)/x2) < self.epsilon) or (count >= self.max_iteration):
                    break
                x0 = x1
                x1 = x2
                count += 1
            steps += "\n" + "the root of f(x) = " + str(x1) + "\n"
            return steps

        except ZeroDivisionError:
            return "There is no solution"

        except OverflowError:
            return "Diverges!"