from methods.abstract_method import *


class Jacobi(AbstractMethod):
    def __init__(self, n, a, b, initial, epsilon, iterations, service):
        self.n = n
        self.a = a
        self.b = b
        self.initial_guess = initial
        # Here we are dividing by 1000 because the value of epsilon does not go below 1 in the GUI
        self.epsilon = epsilon / 1000.0
        self.max_iteration = iterations
        self.service = service

    def execute(self):
        relative_error = [0.0 for _ in range(self.n)]
        x_new = [0.0 for _ in range(self.n)]
        x_old = self.initial_guess
        iteration = 0
        steps = ""
        while iteration < self.max_iteration:
            iteration += 1
            counter = 0
            steps += "Iteration Number " + str(iteration) + ": \n"
            for i in range(self.n):
                numerator = self.b[i]
                for j in range(self.n):
                    if i != j:
                        numerator = self.service.apply_precision(numerator - self.a[i][j] * x_old[j])
                steps += "x" + str(i) + " = " + str(numerator) + " / " + str(self.a[i][i]) + " = "
                try:
                    x_new[i] = self.service.apply_precision(numerator / self.a[i][i])
                except ZeroDivisionError:
                    return "x = infinity" + ", infinity" * len(x_new)
                steps += str(x_new[i]) + "\n"
                if x_new[i] != 0:
                    relative_error[i] = self.service.apply_precision(abs((x_new[i] - x_old[i]) / x_new[i]))
                else:
                    relative_error[i] = 0.0
                if relative_error[i] <= self.epsilon:
                    counter += 1
                steps += "Relative_error(x" + str(i) + ") = " + str(relative_error[i]) + "\n"

            steps+="________________________________\n"
            if counter == self.n:
                break

            for i in range(self.n):
                x_old[i] = x_new[i]

        ans = steps + "approximation of x =  " + " , ".join(str(itt) for itt in x_new)
        return ans
