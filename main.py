import ast
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout
import ctypes

my_app_id = "mycompany.myproduct.subproduct.version"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)


class Runtime_Calculate:
    start_time = 0.0
    end_time = 0.0

    def set_start_time(self):
        self.start_time = time.process_time()

    def set_end_time(self):
        self.end_time = time.process_time()

    def show_runtime(self):
        print('%.16f' % ((self.end_time * self.end_time - self.start_time * self.start_time) / (1000 * (self.end_time + self.start_time))), "millisecond")
        self.start_time = 0.0
        self.end_time = 0.0


class Ui_MainWindow(object):
    precision = 5
    iterations = 10
    epsilon = 5

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Numerical Solver")
        MainWindow.setWindowIcon(QIcon("Course_Icon_LinAlgebra.ico"))
        MainWindow.setLayout(QVBoxLayout())
        MainWindow.resize(452, 484)
        MainWindow.setMaximumHeight(736)
        MainWindow.setFixedWidth(452)
        MainWindow.setFixedHeight(514)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.main_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.main_combobox.setGeometry(QtCore.QRect(20, 10, 411, 22))
        self.main_combobox.setObjectName("main_combobox")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")

        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(120, 30, 191, 81))
        self.info_label.setTextFormat(QtCore.Qt.AutoText)
        self.info_label.setObjectName("info_label")

        self.linear_system_label = QtWidgets.QLabel(self.centralwidget)
        self.linear_system_label.setGeometry(QtCore.QRect(30, 110, 101, 20))
        self.linear_system_label.setObjectName("linear_system_label")

        self.input_textbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_textbox.setGeometry(QtCore.QRect(20, 140, 411, 221))
        self.input_textbox.setObjectName("input_textbox")

        self.precision_label = QtWidgets.QLabel(self.centralwidget)
        self.precision_label.setGeometry(QtCore.QRect(30, 370, 55, 20))
        self.precision_label.setObjectName("precision_label")

        self.precision_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.precision_spinbox.setGeometry(QtCore.QRect(90, 370, 45, 20))
        self.precision_spinbox.setObjectName("precision_spinbox")

        self.max_iteration_label = QtWidgets.QLabel(self.centralwidget)
        self.max_iteration_label.setGeometry(QtCore.QRect(150, 370, 80, 20))
        self.max_iteration_label.setObjectName("max_iteration_label")

        self.max_iteration_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.max_iteration_spinbox.setGeometry(QtCore.QRect(232, 370, 45, 20))
        self.max_iteration_spinbox.setObjectName("max_iteration_spinbox")

        self.relative_error_label = QtWidgets.QLabel(self.centralwidget)
        self.relative_error_label.setGeometry(QtCore.QRect(292, 370, 82, 20))
        self.relative_error_label.setObjectName("relative_error_label")

        self.relative_error_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.relative_error_spinbox.setGeometry(QtCore.QRect(380, 370, 45, 20))
        self.relative_error_spinbox.setObjectName("relative_error_spinbox")

        self.pivoting_type_label = QtWidgets.QLabel(self.centralwidget)
        self.pivoting_type_label.setGeometry(QtCore.QRect(30, 400, 101, 20))
        self.pivoting_type_label.setObjectName("pivoting_type_label")

        self.decomposition_label = QtWidgets.QLabel(self.centralwidget)
        self.decomposition_label.setGeometry(QtCore.QRect(30, 400, 120, 20))
        self.decomposition_label.setObjectName("decomposition_label")

        self.initial_guess_label = QtWidgets.QLabel(self.centralwidget)
        self.initial_guess_label.setGeometry(QtCore.QRect(30, 400, 101, 20))
        self.initial_guess_label.setObjectName("initial_guess_label")

        self.none_pivoting = QtWidgets.QRadioButton(self.centralwidget)
        self.none_pivoting.setGeometry(QtCore.QRect(30, 430, 95, 20))
        self.none_pivoting.setObjectName("none_pivoting")

        self.partial_pivoting = QtWidgets.QRadioButton(self.centralwidget)
        self.partial_pivoting.setGeometry(QtCore.QRect(180, 430, 95, 20))
        self.partial_pivoting.setObjectName("partial_pivoting")

        self.complete_pivoting = QtWidgets.QRadioButton(self.centralwidget)
        self.complete_pivoting.setGeometry(QtCore.QRect(330, 430, 95, 20))
        self.complete_pivoting.setObjectName("complete_pivoting")

        self.initial_guess_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.initial_guess_textbox.setGeometry(QtCore.QRect(20, 430, 411, 22))
        self.initial_guess_textbox.setObjectName("initial_guess_textbox")

        self.decomposition_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.decomposition_combobox.setGeometry(QtCore.QRect(20, 430, 411, 22))
        self.decomposition_combobox.setObjectName("decomposition_combobox")
        self.decomposition_combobox.addItem("")
        self.decomposition_combobox.addItem("")
        self.decomposition_combobox.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 460, 411, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.solve_it)

        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setEnabled(True)
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setObjectName("result_label")
        self.result_label.setMargin(5)

        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(20, 500, 411, 0))
        self.scroll_area.setFixedWidth(411)
        self.scroll_area.setWidget(self.result_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.main_combobox.currentIndexChanged['QString'].connect(self.change)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.runtime = Runtime_Calculate()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical Solver"))

        self.none_pivoting.setText(_translate("MainWindow", "None"))
        self.partial_pivoting.setText(_translate("MainWindow", "Partial"))
        self.complete_pivoting.setText(_translate("MainWindow", "Complete"))
        self.none_pivoting.setChecked(True)

        self.info_label.setText(_translate("MainWindow", "Enter Equations line by line like\n"
                                                    "3, 9, 16\n"
                                                    "5, 12, 1"))
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)

        self.linear_system_label.setText(_translate("MainWindow", "Linear system:"))
        self.pivoting_type_label.setText(_translate("MainWindow", "Pivoting type:"))
        self.initial_guess_label.setText(_translate("MainWindow", "Initial guess:"))

        self.precision_label.setText(_translate("MainWindow", "Precision:"))
        self.max_iteration_label.setText(_translate("MainWindow", "Iterations No:"))
        self.relative_error_label.setText(_translate("MainWindow", "Relative error:"))
        self.decomposition_label.setText(_translate("MainWindow", "Decomposition form:"))

        self.precision_spinbox.setMaximum(10)
        self.precision_spinbox.setMinimum(3)

        self.max_iteration_spinbox.setMaximum(99)
        self.max_iteration_spinbox.setMinimum(2)

        self.relative_error_spinbox.setMaximum(8)
        self.relative_error_spinbox.setMinimum(1)

        self.precision_spinbox.setValue(self.precision)
        self.max_iteration_spinbox.setValue(self.iterations)
        self.relative_error_spinbox.setValue(self.epsilon)

        self.main_combobox.setItemText(0, _translate("MainWindow", "gauss elimination"))
        self.main_combobox.setItemText(1, _translate("MainWindow", "gauss-jordan"))
        self.main_combobox.setItemText(2, _translate("MainWindow", "LU-decomposition"))
        self.main_combobox.setItemText(3, _translate("MainWindow", "jacobi"))
        self.main_combobox.setItemText(4, _translate("MainWindow", "gauss-seidel"))

        self.decomposition_combobox.setItemText(0, _translate("MainWindow", "doolittle form"))
        self.decomposition_combobox.setItemText(1, _translate("MainWindow", "crout form"))
        self.decomposition_combobox.setItemText(2, _translate("MainWindow", "cholesky form"))

        self.pushButton.setText(_translate("MainWindow", "Solve"))

        self.initial_guess_label.hide()
        self.initial_guess_textbox.hide()

        self.decomposition_label.hide()
        self.decomposition_combobox.hide()

        self.max_iteration_label.hide()
        self.max_iteration_spinbox.hide()

        self.relative_error_label.hide()
        self.relative_error_spinbox.hide()

    def change(self):
        if self.main_combobox.currentIndex() == 0 or self.main_combobox.currentIndex() == 1:
            self.pivoting_type_label.show()
            self.none_pivoting.show()
            self.partial_pivoting.show()
            self.complete_pivoting.show()

            self.initial_guess_label.hide()
            self.initial_guess_textbox.hide()

            self.decomposition_label.hide()
            self.decomposition_combobox.hide()

            self.max_iteration_label.hide()
            self.max_iteration_spinbox.hide()

            self.relative_error_label.hide()
            self.relative_error_spinbox.hide()
        elif self.main_combobox.currentIndex() == 3 or self.main_combobox.currentIndex() == 4:
            self.initial_guess_label.show()
            self.initial_guess_textbox.show()

            self.pivoting_type_label.hide()
            self.none_pivoting.hide()
            self.partial_pivoting.hide()
            self.complete_pivoting.hide()

            self.decomposition_label.hide()
            self.decomposition_combobox.hide()

            self.max_iteration_label.show()
            self.max_iteration_spinbox.show()

            self.relative_error_label.show()
            self.relative_error_spinbox.show()
        else:
            self.decomposition_label.show()
            self.decomposition_combobox.show()

            self.pivoting_type_label.hide()
            self.none_pivoting.hide()
            self.partial_pivoting.hide()
            self.complete_pivoting.hide()

            self.initial_guess_label.hide()
            self.initial_guess_textbox.hide()

            self.max_iteration_label.hide()
            self.max_iteration_spinbox.hide()

            self.relative_error_label.hide()
            self.relative_error_spinbox.hide()


    def solve_it(self):

        self.precision = self.precision_spinbox.value()
        self.iterations = self.max_iteration_spinbox.value()
        self.epsilon = self.relative_error_spinbox.value()

        coff = self.input_textbox.toPlainText().split('\n')
        if coff[0].find(',') == -1:
            coff[0] += ','

        n = 0
        a = []
        b = []
        initial = [0 for _ in range(n)]
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
                    self.result_label.setText(
                        f"Row(1) contains {row_size + 1} elements and row({n}) contains {len(a[n - 1]) + 1}"
                        " elements, So your input is invalid")
                    return
            except:
                continue

        if n < row_size:
            self.result_label.setText(
                f"The number of rows({n}) should be one less than the number of columns({row_size + 1})")
            return
        elif n > row_size:
            self.result_label.setText(f"Matrix size must be {row_size + 1}x{row_size + 2}")
            return

        if self.main_combobox.currentText() == "jacobi" or self.main_combobox.currentText() == "gauss-seidel":
            try:
                row_size = len(list(ast.literal_eval(self.initial_guess_textbox.text())))
            except:
                row_size = 0
            if row_size == n:
                initial = list(ast.literal_eval(self.initial_guess_textbox.text()))

        if self.main_combobox.currentText() == "gauss elimination":
            gauss_elimination(self, n, a, b)
        elif self.main_combobox.currentText() == "gauss-jordan":
            gauss_jordan(self, n, a, b)
        elif self.main_combobox.currentText() == "LU-decomposition":
            if self.decomposition_combobox.currentText() == "doolittle form":
                doolittle(self, n, a)
            elif self.decomposition_combobox.currentText() == "crout form":
                crout(self, n, a)
            elif self.decomposition_combobox.currentText() == "cholesky form":
                chelosky(self, n, a)
        elif self.main_combobox.currentText() == "jacobi":
            jacobi(self, n, a, b, initial, self.epsilon, self.iterations)
        elif self.main_combobox.currentText() == "gauss-seidel":
            gauss_seidel(self, n, a, b, initial, self.epsilon, self.iterations)

        s = "\n".join(str(" ".join(str(float(f'%.{self.precision}g' % itt)) for itt in a[it])) + " " + str(b[it]) for it in range(n))

        self.result_label.setText(s)
        self.result_label.adjustSize()
        self.scroll_area.adjustSize()
        MainWindow.setFixedHeight(self.scroll_area.height() + self.scroll_area.y() + 26)


def integer_check(num):
    if num == int(num):
        return int(num)
    return num


def partial_pivoting(n, a, b, k):
    mx = abs(a[k][k])
    row = k
    for i in range(k + 1, n):
        if mx < abs(a[i][k]):
            row = i
            mx = abs(a[i][k])

    a[k], a[row] = a[row], a[k]
    b[k], b[row] = b[row], b[k]


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
    for k in range(n):
        if not decomposition:
            if self.partial_pivoting.isChecked():
                partial_pivoting(n, a, b, k)
            elif self.complete_pivoting.isChecked():
                complete_pivoting(n, a, b, k, o)
            if a[k][k] == 0:
                return False
        for i in range(k + 1, n):
            mult = integer_check(a[i][k] / a[k][k])
            if decomposition:
                a[i][k] = mult
            else:
                a[i][k] = 0
            for j in range(k + 1, n):
                a[i][j] = integer_check(a[i][j] - mult * a[k][j])
            if not decomposition:
                b[i] = integer_check(b[i] - mult * b[k])

    return True


def backward_elimination(n, a, b, o):
    x = [0 for _ in range(n)]

    for k in range(n - 1, -1, -1):
        b[k] = integer_check(b[k] / a[k][k])
        a[k][k] = 1
        for i in range(k - 1, -1, -1):
            b[i] = integer_check(b[i] - a[i][k] * b[k])
            a[i][k] = 0
        x[o[k]] = b[k]

    return x


def backward_substitution(n, a, b, o):
    x = [0 for _ in range(n)]

    x[n - 1] = integer_check(b[n - 1] / a[n - 1][n - 1])
    for i in range(n - 1, -1, -1):
        tot = 0
        for j in range(i + 1, n):
            tot = integer_check(tot + x[j] * a[i][j])
        x[o[i]] = integer_check((b[i] - tot) / a[i][i])

    return x


def gauss_elimination(self, n, a, b):
    self.runtime.set_start_time()
    o = [i for i in range(n)]

    if forward_elimination(self, n, a, b, o, False):
        x = backward_substitution(n, a, b, o)
        for i in range(n):
            print(x[i])
    else:
        print("There is no solution")

    self.runtime.set_end_time()
    self.runtime.show_runtime()


def gauss_jordan(self, n, a, b):
    self.runtime.set_start_time()
    o = [i for i in range(n)]

    if forward_elimination(self, n, a, b, o, False):
        x = backward_elimination(n, a, b, o)
        for i in range(n):
            print(x[i])
    else:
        print("There is no solution")

    self.runtime.set_end_time()
    self.runtime.show_runtime()


def doolittle(self, n, a):
    forward_elimination(self, n, a, [0 for _ in range(n)], [0 for _ in range(n)], True)


def crout(self, n, a):
    doolittle(self, n, a)
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]


def chelosky(self, n, a):
    doolittle(self, n, a)
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j] /= a[i][i]


def jacobi(self, n, a, b, initial_guess, epsilon, max_iteration):
    self.runtime.set_start_time()

    relative_error = [0 for _ in range(n)]
    x_new = [0 for _ in range(n)]
    x_old = initial_guess

    iteration = 0
    while iteration < max_iteration:
        iteration += 1
        counter = 0
        for i in range(n):
            numerator = b[i]
            for j in range(n):
                if i != j:
                    numerator -= a[i][j] * x_old[j]
            x_new[i] = numerator / a[i][i]
            relative_error[i] = abs((x_new[i] - x_old[i]) / x_new[i])
            if relative_error[i] <= epsilon:
                counter += 1

        if counter == n:
            break

        for i in range(n):
            x_old[i] = x_new[i]

    for i in range(n):
        print(x_new[i])

    self.runtime.set_end_time()
    self.runtime.show_runtime()


def gauss_seidel(self, n, a, b, initial_guess, epsilon, max_iteration):
    self.runtime.set_start_time()
    relative_error = [0 for _ in range(n)]
    x = initial_guess

    iteration = 0
    while iteration < max_iteration:
        iteration += 1
        counter = 0
        for i in range(n):
            x_tmp = x[i]
            numerator = b[i]
            for j in range(n):
                if i != j:
                    numerator -= a[i][j] * x[j]
            x[i] = numerator / a[i][i]
            relative_error[i] = abs((x[i] - x_tmp) / x[i])
            if relative_error[i] <= epsilon:
                counter += 1

        if counter == n:
            break

    for i in range(n):
        print(x[i])

    self.runtime.set_end_time()
    self.runtime.show_runtime()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
