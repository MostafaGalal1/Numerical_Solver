from methods.abstract_method import *
from methods.doolittle import *


class Crout(AbstractMethod):
    def __init__(self, n, a, b, service):
        self.n = n
        self.a = a
        self.b = b
        self.service = service

    def execute(self):

        l = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        u = [[0.0 for _ in range(self.n)] for _ in range(self.n)]

        for i in range(self.n):
            u[i][i] = 1
            for j in range(i, self.n):
                tot = 0
                for k in range(i):
                    tot = self.service.apply_precision(tot + (l[j][k] * u[k][i]))
                l[j][i] = self.service.apply_precision(self.a[j][i] - tot)
            for j in range(i, self.n):
                tot = 0
                for k in range(i):
                    tot = self.service.apply_precision(tot + (l[i][k] * u[k][j]))
                if l[i][i] != 0:
                    u[i][j] = self.service.apply_precision((self.a[i][j] - tot) / l[i][i])
                else:
                    return "There is no solution"

        ans = "L = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in l[it])) for it in range(self.n)) + "\n\nU = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in u[it])) for it in range(self.n)) + "\n\nx = " + " , ".join(
            str(it) for it in self.b)

        o = [i for i in range(self.n)]
        x = self.service.forward_substitution(self.n, l, self.b, o)
        if x == "There is no solution":
            return x
        elif x == "Infinite no of solutions":
            return x

        ans += "\n\nY = " + " , ".join(str(it) for it in x)

        y = self.service.backward_substitution(self.n, u, x, o)
        if y == "There is no solution":
            return y
        elif y == "Infinite no of solutions":
            return y

        ans += "\n\nX = " + " , ".join(str(it) for it in y)
        return ans