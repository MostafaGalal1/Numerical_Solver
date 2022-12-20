from methods.abstract_method import *
from methods.doolittle import *


class Chelosky(AbstractMethod):
    def __init__(self, n, a, service):
        self.n = n
        self.a = a
        self.service = service

    def execute(self):
        Doolittle(self.n, self.a, self.service).execute()
        for i in range(self.n):
            for j in range(i + 1, self.n):
               self.a[i][j] = self.service.apply_precision(self.a[i][j] / self.a[i][i])