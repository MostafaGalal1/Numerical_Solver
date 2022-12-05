import ast

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numerical Project")

        self.setLayout(qtw.QVBoxLayout())

        label = qtw.QLabel("")
        label.setFont(qtg.QFont("Helvetica", 12))

        scroll_area = qtw.QScrollArea()
        scroll_area.setWidget(label)
        scroll_area.setWidgetResizable(True)

        button = qtw.QPushButton("Solve", clicked=lambda: solve_it())
        partial_check = qtw.QCheckBox()

        combobox = qtw.QComboBox()
        combobox.addItems(['gauss elimination', 'gauss-jordan', 'LU Decomposition', 'jacobi', 'gauss-seidel'])
        combobox.resize(150, 25)

        textbox = qtw.QPlainTextEdit()
        textbox.resize(300, 300)

        self.layout().addWidget(combobox)
        self.layout().addWidget(textbox)
        self.layout().addWidget(button)
        self.layout().addWidget(partial_check)
        self.layout().addWidget(scroll_area)

        self.show()

        def integer_check(num):
            if num == int(num):
                return int(num)
            return num

        def solve_it():
            coff = textbox.toPlainText().split('\n')
            if coff[0].find(',') == -1:
                coff[0] += ','

            n = 0
            a = []
            b = []
            row_size = 0
            for i in range(len(coff)):
                try:
                    eva = list(ast.literal_eval(coff[i]))
                    a.append(eva[0:len(eva) - 1])
                    b.append(eva[len(eva) - 1])
                    n += 1
                    if n == 1:
                        row_size = len(a[0])
                    if row_size != len(a[n - 1]):
                        label.setText(
                            f"Row(1) contains {row_size + 1} elements and row({n}) contains {len(a[n - 1]) + 1}"
                            " elements, So your input is invalid")
                        return
                except:
                    continue

            if n < row_size:
                label.setText(f"The number of rows({n}) should be one less than the number of columns({row_size + 1})")
                return
            elif n > row_size:
                label.setText(f"Matrix size must be {row_size + 1}x{row_size + 2}")
                return

            if combobox.currentText() == "gauss elimination":
                gauss_elimination(n, a, b)
            elif combobox.currentText() == "gauss-jordan":
                gauss_jordan(n, a, b)

            s = "\n".join(str(" ".join(str(itt) for itt in a[it])) + " " + str(b[it]) for it in range(n))
            label.setText(s)

        def partial_pivoting(n, a, b, k):
            mx = abs(a[k][k])
            row = k
            for i in range(k + 1, n):
                if mx < abs(a[i][k]):
                    row = i
                    mx = abs(a[i][k])

            a[k], a[row] = a[row], a[k]
            b[k], b[row] = b[row], b[k]

        def forward_elimination(n, a, b):
            for k in range(n):
                if partial_check.isChecked():
                    partial_pivoting(n, a, b, k)
                if a[k][k] == 0:
                    return False
                for i in range(k + 1, n):
                    mult = integer_check(a[i][k] / a[k][k])
                    a[i][k] = 0
                    for j in range(k + 1, n):
                        a[i][j] = integer_check(a[i][j] - mult * a[k][j])
                    b[i] = integer_check(b[i] - mult * b[k])

            return True

        def backward_elimination(n, a, b):
            for k in range(n - 1, -1, -1):
                b[k] = integer_check(b[k] / a[k][k])
                a[k][k] = 1
                for i in range(k - 1, -1, -1):
                    b[i] = integer_check(b[i] - a[i][k] * b[k])
                    a[i][k] = 0

        def backward_substitution(n, a, b):
            x = [0 for _ in range(n)]

            x[n - 1] = integer_check(b[n - 1] / a[n - 1][n - 1])
            for i in range(n - 2, -1, -1):
                tot = 0
                for j in range(i + 1, n):
                    tot = integer_check(tot + x[j] * a[i][j])
                    x[i] = integer_check((b[i] - tot) / a[i][i])

            return x

        def gauss_elimination(n, a, b):
            if forward_elimination(n, a, b):
                x = backward_substitution(n, a, b)
                for i in range(n):
                    print(x[i])
            else:
                print("There is no solution")

        def gauss_jordan(n, a, b):
            if forward_elimination(n, a, b):
                backward_elimination(n, a, b)
                for i in range(n):
                    print(b[i])
            else:
                print("There is no solution")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
