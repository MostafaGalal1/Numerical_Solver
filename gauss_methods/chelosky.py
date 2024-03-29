from factories.abstract_method import *
from gauss_methods.doolittle import *


class Chelosky(AbstractMethod):
    def __init__(self, n, a, b, service):
        self.n = n
        self.a = a
        self.b = b
        self.service = service

    def execute(self):
        o = [i for i in range(self.n)]
        flag,ans = self.service.forward_elimination(self.n, self.a, self.b, o, True)
        x = self.service.backward_substitution(self.n,self.a,self.b,o)
        if x == "There is no solution" or x == "Infinite no of solutions":
           return "Matrix can't be decomposed"

        l = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        u = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        d = [[0.0 for _ in range(self.n)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    l[i][j] = 1.0
                    u[i][j] = 1.0
                    d[i][j] = self.a[i][j]
                elif i < j:
                    u[i][j] = self.a[i][j]/self.a[i][i]
                elif i > j:
                    l[i][j] = self.a[i][j]

        ans += "L = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in l[it])) for it in range(self.n)) + "\n\nD = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in d[it])) for it in range(self.n)) + "\n\nU = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in u[it])) for it in range(self.n))

        x = self.service.forward_substitution(self.n, l, self.b, o)
        if x == "There is no solution":
            return ans + "\n\n" + x
        elif x == "Infinite no of solutions":
            return ans + "\n\n" + x

        ans += "\n\nZ = " + " , ".join(str(it) for it in x)

        for i in range (self.n):
            try:
                x[i] = self.service.apply_precision(x[i]  / d[i][i])
            except ZeroDivisionError:
                return ans + "\n\n" + ("Infinite no of solutions" if x[i] == 0 else "There is no solution")
        ans += "\n\nY = " + " , ".join(str(it) for it in x)

        y = self.service.backward_substitution(self.n, u, x, o)
        if y == "There is no solution":
            return ans + "\n\n" + y
        elif y == "Infinite no of solutions":
            return ans + "\n\n" + y

        ans += "\n\nX = " + " , ".join(str(it) for it in y)
        return ans