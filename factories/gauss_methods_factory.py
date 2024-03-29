from gauss_methods.gauss_elimination import *
from gauss_methods.gauss_jordan import *
from gauss_methods.jacobi import *
from gauss_methods.gauss_seidel import *
from gauss_methods.doolittle import *
from gauss_methods.crout import *
from gauss_methods.chelosky import *


class GaussFactory:
    def __init__(self, method, service, n, a, b, initial=None, epsilon=None, iterations=None):
        self.method = method.lower()
        self.service = service
        self.n = n
        self.a = a
        self.b = b
        self.initial = initial
        self.epsilon = epsilon
        self.iterations = iterations

    def create(self):
        if self.method == "gauss elimination":
            return GaussElimination(self.n, self.a, self.b, self.service)
        elif self.method == "gauss-jordan":
            return GaussJordan(self.n, self.a, self.b, self.service)
        elif self.method == "jacobi":
            return Jacobi(self.n, self.a, self.b, self.initial, self.epsilon, self.iterations, self.service)
        elif self.method == "gauss-seidel":
            return GaussSeidel(self.n, self.a, self.b, self.initial, self.epsilon, self.iterations, self.service)
        elif self.method == "doolittle form":
            return Doolittle(self.n, self.a, self.b, self.service)
        elif self.method == "crout form":
            return Crout(self.n, self.a, self.b, self.service)
        elif self.method == "cholesky form":
            return Chelosky(self.n, self.a, self.b, self.service)

