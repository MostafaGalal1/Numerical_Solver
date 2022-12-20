from methods.abstract_method import *


class GaussElimination(AbstractMethod):
    def __init__(self, n, a, b, service):
        self.n = n
        self.a = a
        self.b = b
        self.service = service

    def execute(self):
        o = [i for i in range(self.n)]

        if self.service.forward_elimination(self.n, self.a, self.b, o, False):
            x = self.service.backward_substitution(self.n, self.a, self.b, o)
            if x == "There is no solution" or x == "Infinite no of solutions":
                return x
        else:
            return "There is no solution"

        ans = "A | b = \n" + "\n".join(str(" , ".join(str(itt) for itt in self.a[it])) + " , " + str(self.b[it]) for it in range(self.n)) + "\n\nx = " + " , ".join(str(itt) for itt in x)
        return ans