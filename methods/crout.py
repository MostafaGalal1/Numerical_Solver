from methods.abstract_method import *
from methods.doolittle import *


class Crout(AbstractMethod):
    def __init__(self, n, a, service):
        self.n = n
        self.a = a
        self.service = service

    def execute(self):
        Doolittle(self.n, self.a, self.service).execute()
        for i in range(self.n):
            for j in range(i + 1, self.n):
               self.a[i][j], self.a[j][i] = self.a[j][i], self.a[i][j]