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
            lists = []
            while True:
                list = []
                x1 = self.service.apply_precision(x0 - f(x0) / dif(x0))
                if (abs(x0 - x1) < self.epsilon) or (count >= self.max_iteration):
                    break
                list.append(count)
                list.append(x0)
                list.append(x1)
                list.append(f(x0))
                list.append(f(x1))
                list.append(x1-x0)
                lists.append(list)
                x0 = x1
                print("the value of the root in iteration " + str(count) + " is " + str(x1))
                count += 1
            print(lists)
            print("*********************************")
            return lists
        except ZeroDivisionError:
            return "There is no solution"