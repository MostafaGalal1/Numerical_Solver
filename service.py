import numpy as np


class Service:

    def __init__(self, precision, none_pivoting, partial_pivoting, complete_pivoting):
        self.precision = precision
        self.none_pivoting = none_pivoting
        self.partial_pivoting = partial_pivoting
        self.complete_pivoting = complete_pivoting

    def apply_precision(self, num):
        return float(
            np.format_float_positional(num, precision=self.precision, unique=False, fractional=False, trim='k'))

    @staticmethod
    def partial_pivoting(n, a, b, k):
        mx = abs(a[k][k])
        row = k
        for i in range(k + 1, n):
            if mx < abs(a[i][k]):
                row = i
                mx = abs(a[i][k])

        a[k], a[row] = a[row], a[k]
        b[k], b[row] = b[row], b[k]

    @staticmethod
    def complete_pivoting(n, a, b, k, o):
        mx = abs(a[k][k])
        row = k
        col = k
        for i in range(k, n):
            for j in range(k, n):
                if mx < abs(a[i][j]):
                    row = i
                    col = j
                    mx = abs(a[i][j])

        a[k], a[row] = a[row], a[k]
        b[k], b[row] = b[row], b[k]
        o[k], o[col] = o[col], o[k]
        for i in range(n):
            a[i][k], a[i][col] = a[i][col], a[i][k]

    def forward_elimination(self, n, a, b, o, decomposition):
        pivot = 0
        for k in range(n):
            if not decomposition:
                if self.partial_pivoting:
                    Service.partial_pivoting(n, a, b, k)
                elif self.complete_pivoting:
                    Service.complete_pivoting(n, a, b, k, o)
                else:
                    if a[k][k] == 0:
                        return False
            for i in range(k + 1, n):
                if (not self.none_pivoting) and a[k][k + pivot] == 0:
                    pivot += 1
                    continue
                mult = self.apply_precision(a[i][k + pivot] / a[k][k + pivot])
                if decomposition:
                    a[i][k + pivot] = mult
                else:
                    a[i][k + pivot] = 0
                for j in range(k + pivot + 1, n):
                    a[i][j] = self.apply_precision(a[i][j] - mult * a[k][j])
                if not decomposition:
                    b[i] = self.apply_precision(b[i] - mult * b[k])

        return True

    def backward_elimination(self, n, a, b, o):
        x = [0.0 for _ in range(n)]

        infinite = False
        for k in range(n - 1, -1, -1):
            if a[k][k] != 0:
                b[k] = self.apply_precision(b[k] / a[k][k])
                a[k][k] = 1
            else:
                if b[k] == 0:
                    infinite = True
                    continue
                else:
                    return "There is no solution"
            for i in range(k - 1, -1, -1):
                b[i] = self.apply_precision(b[i] - a[i][k] * b[k])
                a[i][k] = 0
            x[o[k]] = b[k]

        if infinite:
            return "Infinite no of solutions"

        return x

    def backward_substitution(self, n, a, b, o):
        x = [0.0 for _ in range(n)]

        infinite = False
        if a[n - 1][n - 1] != 0:
            x[n - 1] = self.apply_precision(b[n - 1] / a[n - 1][n - 1])
        else:
            if b[n - 1] == 0:
                infinite = True
            else:
                return "There is no solution"

        for i in range(n - 1, -1, -1):
            tot = 0
            for j in range(i + 1, n):
                tot = self.apply_precision(tot + x[j] * a[i][j])
            if a[i][i] != 0:
                x[o[i]] = self.apply_precision((b[i] - tot) / a[i][i])
            else:
                if b[i] - tot == 0:
                    infinite = True
                else:
                    return "There is no solution"

        if infinite:
            return "Infinite no of solutions"

        return x
