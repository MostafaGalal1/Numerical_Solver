from factories.abstract_method import *


class GaussJordan(AbstractMethod):
    def __init__(self, n, a, b, service):
        self.n = n
        self.a = a
        self.b = b
        self.service = service

    def execute(self):
        o = [i for i in range(self.n)]
        flag,ans1 = self.service.forward_elimination(self.n, self.a, self.b, o, False)
        if flag :
            x,ans2 = self.service.backward_elimination(self.n, self.a, self.b, o)
            if x == "There is no solution" or x == "Infinite no of solutions":
                return x
        else:
            return "There is no solution"

        ans = ans1 + ans2 + "x = " + " , ".join(str(itt) for itt in x)
        return ans