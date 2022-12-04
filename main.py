import ast

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numerical Project")

        self.setLayout(qtw.QVBoxLayout())

        l = qtw.QLabel("SFDghj")
        l.setFont(qtg.QFont("Helvetica", 18))

        self.layout().addWidget(l)

        e = qtw.QLineEdit()
        e.setObjectName("name")
        e.setText("sdfdf")

        self.layout().addWidget(e)

        b = qtw.QPushButton("press",
                            clicked = lambda: press_it())

        self.layout().addWidget(b)

        combobox =qtw.QComboBox()
        combobox.addItems(['gauss elimination', 'gauss-jordan', 'LU Decomposition', 'jacobi', 'gauss-seidel'])
        combobox.resize(150, 25)

        textbox = qtw.QPlainTextEdit()
        textbox.resize(300, 300)

        self.layout().addWidget(textbox)
        self.layout().addWidget(combobox)

        self.show()

        def press_it():
            coff = textbox.toPlainText().split('\n')
            n = 3
            a = []
            b = []
            for i in range(len(coff)):
                eva = list(ast.literal_eval(textbox.toPlainText().split('\n')[i]))
                a.append(eva[0:n])
                b.append(eva[n])

            print(a)
            print(b)
            gauss_elimination(n, a, b)
            s = "\n".join(str(" ".join(str(itt) for itt in a[it])) for it in range(n))
            l.setText(s)

        def gauss_elimination(n, a, b):
            x = [0 for i in range(n)]
            print(len(x))

            for k in range(n-1):
                for i in range(k+1, n):
                    mult = a[i][k] / a[k][k]
                    a[i][k] = 0
                    for j in range(k+1, n):
                        a[i][j] -= mult * a[k][j]
                    b[i] -= mult * b[k]

            for i in range(n):
                for j in range(n):
                    print(a[i][j], end=' ')
                print(b[i])

            x[n - 1] = b[n - 1] / a[n - 1][n - 1]
            for i in range(n-2, -1, -1):
                sum = 0
                for j in range(i+1, n):
                    sum += x[j] * a[i][j]
                    x[i] = (b[i] - sum) / a[i][i]

            for i in range(n):
                print(x[i])


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
