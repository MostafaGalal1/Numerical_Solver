from methods.abstract_method import *


class GaussSeidel(AbstractMethod):
    def __init__(self, n, a, b, initial, epsilon, iterations, service):
        self.n = n
        self.a = a
        self.b = b
        self.initial_guess = initial
        self.epsilon = epsilon
        self.max_iteration = iterations
        self.service = service

    def execute(self):
        relative_error = [0.0 for _ in range(self.n)]
        x = self.initial_guess

        iteration = 0
        while iteration < self.max_iteration:
            iteration += 1
            counter = 0
            for i in range(self.n):
                x_tmp = x[i]
                numerator = self.b[i]
                for j in range(self.n):
                    if i != j:
                        numerator = self.service.apply_precision(numerator - self.a[i][j] * x[j])
                x[i] = self.service.apply_precision(numerator / self.a[i][i])
                relative_error[i] = self.service.apply_precision(abs((x[i] - x_tmp) / x[i]))
                if relative_error[i] <= self.epsilon:
                    counter += 1

            if counter == self.n:
                break

        for i in range(self.n):
            print(x[i])
