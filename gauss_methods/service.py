import numpy as np


class Service:

    def __init__(self, precision, none_pivoting = None, partial_pivoting = None, complete_pivoting = None):
        self.precision = precision
        self.none_pivoting = none_pivoting
        self.partial_pivoting = partial_pivoting
        self.complete_pivoting = complete_pivoting

    def apply_precision(self, num):
        return float(np.format_float_positional(num, precision=self.precision+1, unique=False, fractional=False, trim='k'))

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
        ans = ""
        for k in range(n):
            if self.partial_pivoting:
                Service.partial_pivoting(n, a, b, k)
            elif self.complete_pivoting:
                Service.complete_pivoting(n, a, b, k, o)

            if a[k][k] == 0 and self.none_pivoting:
                return False,None
            for i in range(k + 1, n):
                if (not self.none_pivoting) and a[k - pivot][k] == 0:
                    pivot += 1
                    continue
                mult = self.apply_precision(a[i - pivot][k] / a[k - pivot][k])
                if decomposition:
                    a[i - pivot][k] = mult
                else:
                    a[i - pivot][k] = 0
                for j in range(k + 1, n):
                    a[i-pivot][j] = self.apply_precision(a[i-pivot][j] - mult * a[k-pivot][j])
                if not decomposition:
                    b[i-pivot] = self.apply_precision(b[i-pivot] - mult * b[k-pivot])

                ans += "A | b = \n" + "\n".join(str(" , ".join(str(itt) for itt in a[it])) + " , " + str(b[it]) for it in range(n)) + "\n\n"
        return True,ans

    def backward_elimination(self, n, a, b, o):
        x = [b[i] for i in range(n)]
        ans = ""
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
                    return "There is no solution",None
            for i in range(k - 1, -1, -1):
                b[i] = self.apply_precision(b[i] - a[i][k] * b[k])
                x[o[i]] = b[i]
                a[i][k] = 0
            x[o[k]] = b[k]
            ans += "A | b = \n" + "\n".join(str(" , ".join(str(itt) for itt in a[it])) + " , " + str(x[it]) for it in range(n)) + "\n\n"

        if infinite:
            return "Infinite no of solutions",None

        return x,ans

    def forward_substitution(self, n, a, b, o):
        x = [0.0 for _ in range(n)]

        infinite = False
        if a[0][0] != 0:
            x[0] = self.apply_precision(b[0] / a[0][0])
        else:
            if b[0] == 0:
                infinite = True
            else:
                return "There is no solution"

        for i in range(n):
            tot = 0
            for j in range(i):
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
