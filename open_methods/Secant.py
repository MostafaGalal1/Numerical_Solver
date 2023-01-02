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
            lists = []
            f = lambda x: eval(self.function)
            x0 = self.x_lower
            x1 = self.x_upper
            while True:
                list = []
                x2 = self.service.apply_precision(x1 - self.service.apply_precision(f(x1) * (x1 - x0) / self.service.apply_precision(f(x1) - f(x0))))
                if (x2 != 0 and self.service.apply_precision(abs(x2 - x1)/x2) < self.epsilon) or (count >= self.max_iteration):
                    break
                list.append(count)
                list.append(x0)
                list.append(x1)
                list.append(f(x0))
                list.append(f(x1))
                list.append(x2)
                list.append(x2 - x1)
                lists.append(list)
                x0 = x1
                x1 = x2
                print("the value of the root in iteration " + str(count) + " is " + str(x2))
                count += 1
            print(lists)
            return lists

        except ZeroDivisionError:
            return "There is no solution"

        except OverflowError:
            return "Diverges!"