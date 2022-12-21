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

        for i in range(0, self.n):
            u[i][i] = 1

        for i in range(0, self.n):
            for j in range(i, self.n):
                tot = 0
                for k in range(0, i):
                    tot = tot + (l[j][k] * u[k][i])
                l[j][i] = self.a[j][i] - tot
            for j in range(i, self.n):
                tot = 0
                for k in range(0, i):
                    tot = tot + (l[i][k] * u[k][j])
                try:
                    u[i][j] = (self.a[i][j] - tot) / l[i][i]
                except ZeroDivisionError:
                    return "There is no solution"

        ans = "L = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in l[it])) for it in range(self.n)) + "\n\nU = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in u[it])) for it in range(self.n)) + "\n\nx = " + " , ".join(
            str(it) for it in self.b)

        x = GaussJordan(self.n, l, self.b, self.service).execute()
        if x == "There is no solution":
            return x
        elif x == "Infinite no of solutions":
            return x
        ans += "\n\nY = " + " , ".join(str(it) for it in self.b)

        x = GaussJordan(self.n, u, self.b, self.service).execute()
        if x == "There is no solution":
            return x
        elif x == "Infinite no of solutions":
            return x

        ans += "\n\nX = " + " , ".join(str(it) for it in self.b)
        return ans