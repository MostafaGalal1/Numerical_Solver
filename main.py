import ast

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout
import ctypes

my_app_id = "mycompany.myproduct.subproduct.version"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

class Ui_MainWindow(object):
    epsilon = 1e-9

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Numerical Solver")
        MainWindow.setWindowIcon(QIcon("Course_Icon_LinAlgebra.ico"))
        MainWindow.setLayout(QVBoxLayout())
        MainWindow.resize(452, 484)
        MainWindow.setMaximumHeight(736)
        MainWindow.setFixedWidth(452)
        MainWindow.setFixedHeight(484)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 400, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 400, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(330, 400, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 400, 411, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit_2 = QtWidgets.QLabel(self.centralwidget)
        self.plainTextEdit_2.setEnabled(True)
        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(20, 470, 411, 0))
        self.scroll_area.setFixedWidth(411)
        self.scroll_area.setWidget(self.plainTextEdit_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setMargin(5)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 140, 411, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 191, 81))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 370, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 101, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 411, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 101, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.pressed.connect(self.solve_it)
        self.pushButton.setGeometry(QtCore.QRect(20, 430, 411, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.currentIndexChanged['QString'].connect(self.change)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical Solver"))
        self.radioButton.setText(_translate("MainWindow", "None"))
        self.radioButton_2.setText(_translate("MainWindow", "Partial"))
        self.radioButton_3.setText(_translate("MainWindow", "Complete"))
        self.radioButton.setChecked(True)

        self.label.setText(_translate("MainWindow", "Enter Equations line by line like\n"
                                                                "3, 9, 16\n"
                                                                "5, 12, 1"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText(_translate("MainWindow", "Initial guess:"))
        self.label_2.setText(_translate("MainWindow", "Linear system:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "gauss elimination"))
        self.comboBox.setItemText(1, _translate("MainWindow", "gauss-jordan"))
        self.comboBox.setItemText(2, _translate("MainWindow", "LU-decomposition"))
        self.comboBox.setItemText(3, _translate("MainWindow", "jacobi"))
        self.comboBox.setItemText(4, _translate("MainWindow", "gauss-seidel"))
        self.label_4.setText(_translate("MainWindow", "Pivoting type:"))
        self.pushButton.setText(_translate("MainWindow", "Solve"))
        self.label_3.hide()
        self.lineEdit.hide()

    def change(self):
        if self.comboBox.currentIndex() == 0 or self.comboBox.currentIndex() == 1:
            self.label_4.show()
            self.radioButton.show()
            self.radioButton_2.show()
            self.radioButton_3.show()
            self.label_3.hide()
            self.lineEdit.hide()
        elif self.comboBox.currentIndex() == 3 or self.comboBox.currentIndex() == 4:
            self.label_3.show()
            self.lineEdit.show()
            self.label_4.hide()
            self.radioButton.hide()
            self.radioButton_2.hide()
            self.radioButton_3.hide()

    def solve_it(self, epsilon=epsilon):
        coff = self.plainTextEdit.toPlainText().split('\n')
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
                    self.plainTextEdit_2.setText(
                        f"Row(1) contains {row_size + 1} elements and row({n}) contains {len(a[n - 1]) + 1}"
                        " elements, So your input is invalid")
                    return
            except:
                continue

        if n < row_size:
            self.plainTextEdit_2.setText(
                f"The number of rows({n}) should be one less than the number of columns({row_size + 1})")
            return
        elif n > row_size:
            self.plainTextEdit_2.setText(f"Matrix size must be {row_size + 1}x{row_size + 2}")
            return

        if self.comboBox.currentText() == "jacobi" or self.comboBox.currentText() == "gauss-seidel":
            initial = [0 for _ in range(n)]
            try:
                row_size = len(list(ast.literal_eval(self.lineEdit.text())))
            except:
                row_size = 0
            if row_size == n:
                initial = list(ast.literal_eval(self.lineEdit.text()))

        if self.comboBox.currentText() == "gauss elimination":
            gauss_elimination(self, n, a, b)
        elif self.comboBox.currentText() == "gauss-jordan":
            gauss_jordan(self, n, a, b)
        elif self.comboBox.currentText() == "jacobi":
            jacobi(n, a, b, initial, epsilon, 100)
        elif self.comboBox.currentText() == "gauss-seidel":
            gauss_seidel(n, a, b, initial, epsilon, 100)

        s = "\n".join(str(" ".join(str(itt) for itt in a[it])) + " " + str(b[it]) for it in range(n))
        self.plainTextEdit_2.setText(s)
        self.plainTextEdit_2.adjustSize()
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


def forward_elimination(self, n, a, b, o):
    for k in range(n):
        if self.radioButton_2.isChecked():
            partial_pivoting(n, a, b, k)
        elif self.radioButton_3.isChecked():
            complete_pivoting(n, a, b, k, o)
        if a[k][k] == 0:
            return False
        for i in range(k + 1, n):
            mult = integer_check(a[i][k] / a[k][k])
            a[i][k] = 0
            for j in range(k + 1, n):
                a[i][j] = integer_check(a[i][j] - mult * a[k][j])
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
    o = [i for i in range(n)]

    if forward_elimination(self, n, a, b, o):
        x = backward_substitution(n, a, b, o)
        for i in range(n):
            print(x[i])
    else:
        print("There is no solution")


def gauss_jordan(self, n, a, b):
    o = [i for i in range(n)]

    if forward_elimination(self, n, a, b, o):
        x = backward_elimination(n, a, b, o)
        for i in range(n):
            print(x[i])
    else:
        print("There is no solution")


def jacobi(n, a, b, initial_guess, epsilon, max_iteration):
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


def gauss_seidel(n, a, b, initial_guess, epsilon, max_iteration):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())