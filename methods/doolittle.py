from methods.abstract_method import *


class Doolittle(AbstractMethod):
    def __init__(self, n, a, service):
        self.n = n
        self.a = a
        self.service = service

    def execute(self):
       self.service.forward_elimination(self.n, self.a, [0 for _ in range(self.n)], [0 for _ in range(self.n)], True)