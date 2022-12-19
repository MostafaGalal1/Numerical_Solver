from methods.abstract_method import *


class GaussJordan(AbstractMethod):
    def __init__(self, n, a, b, service):
        self.n = n
        self.a = a
        self.b = b
        self.service = service

    def execute(self):
        o = [i for i in range(self.n)]

        if self.service.forward_elimination(self.n, self.a, self.b, o, False):
            x = self.service.backward_substitution(self.n, self.a, self.b, o)
            for i in range(self.n):
                print(x[i])
        else:
            print("There is no solution")
