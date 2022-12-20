from methods.abstract_method import *
from methods.gauss_elimination import *
from methods.gauss_jordan import *

class Doolittle(AbstractMethod):
    def __init__(self, n, a, b, service):
        self.n = n
        self.a = a
        self.b = b
        self.service = service

    def execute(self):
        flag,ans = self.service.forward_elimination(self.n, self.a, [0 for _ in range(self.n)], [0 for _ in range(self.n)], True)
        if not flag:
           return "There is no solution"

        l = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        u = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    l[i][j] = 1.0
                    u[i][j] = self.a[i][j]
                elif i < j:
                    u[i][j] = self.a[i][j]
                elif i > j:
                    l[i][j] = self.a[i][j]

        ans += "L = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in l[it])) for it in range(self.n)) + "\n\nU = \n" + "\n".join(
            str(" , ".join(str(itt) for itt in u[it])) for it in range(self.n))

        x = GaussJordan(self.n, l, self.b, self.service).execute()
        if x == "There is no solution":
            return x
        elif x == "Infinite no of solutions":
            return x
        print(self.b)
        ans += "\n\nY = " + " , ".join(str(it) for it in self.b)
        x = GaussJordan(self.n, u, self.b, self.service).execute()
        if x == "There is no solution":
            return x
        elif x == "Infinite no of solutions":
            return x

        ans += "\n\nX = " + " , ".join(str(it) for it in self.b)
        return ans
