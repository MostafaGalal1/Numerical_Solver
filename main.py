import ast

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numerical Project")

        self.setLayout(qtw.QVBoxLayout())

        label = qtw.QLabel("")
        label.setFont(qtg.QFont("Helvetica", 18))

        button = qtw.QPushButton("press", clicked=lambda: press_it())

        combobox = qtw.QComboBox()
        combobox.addItems(['gauss elimination', 'gauss-jordan', 'LU Decomposition', 'jacobi', 'gauss-seidel'])
        combobox.resize(150, 25)

        textbox = qtw.QPlainTextEdit()
        textbox.resize(300, 300)

        self.layout().addWidget(combobox)
        self.layout().addWidget(textbox)
        self.layout().addWidget(button)
        self.layout().addWidget(label)

        self.show()

        def press_it():
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
                    a.append(eva[0:len(eva)-1])
                    b.append(eva[len(eva)-1])
                    print(eva, a[n], b[n])
                    n += 1
                    if n == 1:
                        row_size = len(a[0])
                    if row_size != len(a[n-1]):
                        label.setText(
                            f"Row(1) contains {row_size + 1} elements and row({n}) contains {len(a[n - 1]) + 1} elements, So your input is invalid")
                        return
                except:
                    continue

            print(row_size, n)

            if n < row_size:
                label.setText(f"The number of rows({n}) should be one less than the number of columns({row_size + 1})")
                return
            elif n > row_size:
                label.setText(f"Matrix size must be {row_size + 1}x{row_size + 2}")
                return

            print(a)
            print(b)
            gauss_jordan(n, a, b)
            s = "\n".join(str(" ".join(str(itt) for itt in a[it])) + " " + str(b[it]) for it in range(n))
            label.setText(s)

        def forward_elimination(n, a, b):
            for k in range(n - 1):
                for i in range(k + 1, n):
                    mult = a[i][k] / a[k][k]
                    a[i][k] = 0
                    for j in range(k + 1, n):
                        a[i][j] -= mult * a[k][j]
                    b[i] -= mult * b[k]

        def backward_elimination(n, a, b):
            for k in range(n - 1, -1, -1):
                b[k] /= a[k][k]
                a[k][k] = 1
                for i in range(k - 1, -1, -1):
                    b[i] -= a[i][k] * b[k]
                    a[i][k] = 0

        def backward_substitution(n, a, b):
            x = [0 for i in range(n)]

            x[n - 1] = b[n - 1] / a[n - 1][n - 1]
            for i in range(n - 2, -1, -1):
                sum = 0
                for j in range(i + 1, n):
                    sum += x[j] * a[i][j]
                    x[i] = (b[i] - sum) / a[i][i]

            return x

        def gauss_elimination(n, a, b):
            forward_elimination(n, a, b)
            x = backward_substitution(n, a, b)
            for i in range(n):
                print(x[i])

        def gauss_jordan(n, a, b):
            forward_elimination(n, a, b)
            backward_elimination(n, a, b)
            for i in range(n):
                print(b[i] / a[i][i])


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
