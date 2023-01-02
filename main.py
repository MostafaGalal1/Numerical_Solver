import ast
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout
import ctypes
from symtable import *
from sympy import *
from gauss_methods.service import *
from factories.gauss_methods_factory import *
from factories.root_methods_factory import *

my_app_id = "mycompany.myproduct.subproduct.version"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)


class Ui_MainWindow(object):
    linearView = True
    default_precision = 5
    default_iterations = 10
    default_epsilon = 5
    precision = default_precision
    iterations = default_iterations
    epsilon = default_epsilon

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Numerical Solver")
        MainWindow.setWindowIcon(QIcon("Course_Icon_LinAlgebra.ico"))
        MainWindow.setLayout(QVBoxLayout())
        MainWindow.resize(452, 540)
        MainWindow.setMaximumHeight(726)
        MainWindow.setFixedWidth(452)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 26))

        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionLinear = QtWidgets.QAction(MainWindow)
        self.actionLinear.setObjectName("actionLinear")
        self.actionNonlinear = QtWidgets.QAction(MainWindow)
        self.actionNonlinear.setObjectName("actionNonlinear")

        self.menuMenu.addAction(self.actionLinear)
        self.menuMenu.addAction(self.actionNonlinear)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.LinearWidgetContents = QtWidgets.QWidget()
        self.NonlinearWidgetContents = QtWidgets.QWidget()

        self.LinearscrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.LinearscrollArea.setGeometry(QtCore.QRect(0, 0, 452, 700))
        self.LinearscrollArea.setWidgetResizable(True)
        self.LinearscrollArea.setObjectName("LinearscrollArea")

        self.NonlinearscrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.NonlinearscrollArea.setGeometry(QtCore.QRect(0, 0, 452, 700))
        self.NonlinearscrollArea.setWidgetResizable(True)
        self.NonlinearscrollArea.setObjectName("NonlinearscrollArea")

        self.LinearscrollArea.setWidget(self.LinearWidgetContents)
        self.NonlinearscrollArea.setWidget(self.NonlinearWidgetContents)

        self.main_combobox = QtWidgets.QComboBox(self.LinearWidgetContents)
        self.main_combobox.setGeometry(QtCore.QRect(20, 10, 411, 22))
        self.main_combobox.setObjectName("main_combobox")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")
        self.main_combobox.addItem("")

        self.info_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.info_label.setGeometry(QtCore.QRect(120, 30, 191, 81))
        self.info_label.setTextFormat(QtCore.Qt.AutoText)
        self.info_label.setObjectName("info_label")

        self.linear_system_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.linear_system_label.setGeometry(QtCore.QRect(30, 110, 101, 20))
        self.linear_system_label.setObjectName("linear_system_label")

        self.input_textbox = QtWidgets.QPlainTextEdit(self.LinearWidgetContents)
        self.input_textbox.setGeometry(QtCore.QRect(20, 140, 411, 221))
        self.input_textbox.setObjectName("input_textbox")

        self.precision_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.precision_label.setGeometry(QtCore.QRect(30, 370, 55, 20))
        self.precision_label.setObjectName("precision_label")

        self.precision_spinbox = QtWidgets.QSpinBox(self.LinearWidgetContents)
        self.precision_spinbox.setGeometry(QtCore.QRect(80, 370, 45, 20))
        self.precision_spinbox.setObjectName("precision_spinbox")

        self.max_iteration_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.max_iteration_label.setGeometry(QtCore.QRect(135, 370, 80, 20))
        self.max_iteration_label.setObjectName("max_iteration_label")

        self.max_iteration_spinbox = QtWidgets.QSpinBox(self.LinearWidgetContents)
        self.max_iteration_spinbox.setGeometry(QtCore.QRect(207, 370, 45, 20))
        self.max_iteration_spinbox.setObjectName("max_iteration_spinbox")

        self.relative_error_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.relative_error_label.setGeometry(QtCore.QRect(262, 370, 120, 20))
        self.relative_error_label.setObjectName("relative_error_label")

        self.relative_error_spinbox = QtWidgets.QSpinBox(self.LinearWidgetContents)
        self.relative_error_spinbox.setGeometry(QtCore.QRect(380, 370, 45, 20))
        self.relative_error_spinbox.setObjectName("relative_error_spinbox")

        self.pivoting_type_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.pivoting_type_label.setGeometry(QtCore.QRect(30, 400, 101, 20))
        self.pivoting_type_label.setObjectName("pivoting_type_label")

        self.decomposition_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.decomposition_label.setGeometry(QtCore.QRect(30, 400, 120, 20))
        self.decomposition_label.setObjectName("decomposition_label")

        self.initial_guess_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.initial_guess_label.setGeometry(QtCore.QRect(30, 400, 101, 20))
        self.initial_guess_label.setObjectName("initial_guess_label")

        self.none_pivoting = QtWidgets.QRadioButton(self.LinearWidgetContents)
        self.none_pivoting.setGeometry(QtCore.QRect(30, 430, 95, 20))
        self.none_pivoting.setObjectName("none_pivoting")

        self.partial_pivoting = QtWidgets.QRadioButton(self.LinearWidgetContents)
        self.partial_pivoting.setGeometry(QtCore.QRect(180, 430, 95, 20))
        self.partial_pivoting.setObjectName("partial_pivoting")

        self.complete_pivoting = QtWidgets.QRadioButton(self.LinearWidgetContents)
        self.complete_pivoting.setGeometry(QtCore.QRect(330, 430, 95, 20))
        self.complete_pivoting.setObjectName("complete_pivoting")

        self.initial_guess_textbox = QtWidgets.QLineEdit(self.LinearWidgetContents)
        self.initial_guess_textbox.setGeometry(QtCore.QRect(20, 430, 411, 22))
        self.initial_guess_textbox.setObjectName("initial_guess_textbox")

        self.decomposition_combobox = QtWidgets.QComboBox(self.LinearWidgetContents)
        self.decomposition_combobox.setGeometry(QtCore.QRect(20, 430, 411, 22))
        self.decomposition_combobox.setObjectName("decomposition_combobox")
        self.decomposition_combobox.addItem("")
        self.decomposition_combobox.addItem("")
        self.decomposition_combobox.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.LinearWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(20, 460, 411, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.solve_linear)

        self.result_label = QtWidgets.QLabel(self.LinearWidgetContents)
        self.result_label.setEnabled(True)
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setObjectName("result_label")
        self.result_label.setMargin(5)

        self.scroll_area = QtWidgets.QScrollArea(self.LinearWidgetContents)
        self.scroll_area.setGeometry(QtCore.QRect(20, 500, 411, 0))
        self.scroll_area.setFixedWidth(411)
        self.scroll_area.setMaximumHeight(195)
        self.scroll_area.setWidget(self.result_label)

        self.non_main_combobox = QtWidgets.QComboBox(self.NonlinearWidgetContents)
        self.non_main_combobox.setGeometry(QtCore.QRect(20, 10, 411, 22))
        self.non_main_combobox.setObjectName("non_main_combobox")
        self.non_main_combobox.addItem("")
        self.non_main_combobox.addItem("")
        self.non_main_combobox.addItem("")
        self.non_main_combobox.addItem("")
        self.non_main_combobox.addItem("")

        self.non_info_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.non_info_label.setGeometry(QtCore.QRect(120, 30, 180, 60))
        self.non_info_label.setTextFormat(QtCore.Qt.AutoText)
        self.non_info_label.setObjectName("info_label")

        self.fx_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.fx_label.setGeometry(QtCore.QRect(30, 110, 101, 20))
        self.fx_label.setObjectName("fx_label")

        self.fx_textbox = QtWidgets.QPlainTextEdit(self.NonlinearWidgetContents)
        self.fx_textbox.setGeometry(QtCore.QRect(60, 110, 371, 21))
        self.fx_textbox.setObjectName("fx_textbox")
        self.fx_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.gx_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.gx_label.setGeometry(QtCore.QRect(172, 150, 101, 20))
        self.gx_label.setObjectName("gx_label")

        self.gx_textbox = QtWidgets.QPlainTextEdit(self.NonlinearWidgetContents)
        self.gx_textbox.setGeometry(QtCore.QRect(202, 150, 229, 21))
        self.gx_textbox.setObjectName("gx_textbox")
        self.gx_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.fdashx_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.fdashx_label.setGeometry(QtCore.QRect(172, 150, 101, 20))
        self.fdashx_label.setObjectName("fdashx_label")

        self.fdashx_textbox = QtWidgets.QPlainTextEdit(self.NonlinearWidgetContents)
        self.fdashx_textbox.setGeometry(QtCore.QRect(202, 150, 229, 21))
        self.fdashx_textbox.setObjectName("fdashx_textbox")
        self.fdashx_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.xl_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.xl_label.setGeometry(QtCore.QRect(30, 150, 56, 20))
        self.xl_label.setObjectName("xl_label")

        self.xu_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.xu_label.setGeometry(QtCore.QRect(182, 150, 56, 20))
        self.xu_label.setObjectName("xu_label")

        self.xo_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.xo_label.setGeometry(QtCore.QRect(30, 150, 56, 20))
        self.xo_label.setObjectName("xo_label")

        self.xl_textbox = QtWidgets.QTextEdit(self.NonlinearWidgetContents)
        self.xl_textbox.setGeometry(QtCore.QRect(55, 150, 100, 20))
        self.xl_textbox.setObjectName("xl_textbox")
        self.xl_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.xu_textbox = QtWidgets.QTextEdit(self.NonlinearWidgetContents)
        self.xu_textbox.setGeometry(QtCore.QRect(207, 150, 100, 20))
        self.xu_textbox.setObjectName("xu_textbox")
        self.xu_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.xo_textbox = QtWidgets.QTextEdit(self.NonlinearWidgetContents)
        self.xo_textbox.setGeometry(QtCore.QRect(55, 150, 100, 20))
        self.xo_textbox.setObjectName("xo_textbox")
        self.xo_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.non_precision_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.non_precision_label.setGeometry(QtCore.QRect(30, 190, 55, 20))
        self.non_precision_label.setObjectName("precision_label")

        self.non_precision_spinbox = QtWidgets.QSpinBox(self.NonlinearWidgetContents)
        self.non_precision_spinbox.setGeometry(QtCore.QRect(80, 190, 45, 20))
        self.non_precision_spinbox.setObjectName("precision_spinbox")

        self.non_max_iteration_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.non_max_iteration_label.setGeometry(QtCore.QRect(135, 190, 80, 20))
        self.non_max_iteration_label.setObjectName("max_iteration_label")

        self.non_max_iteration_spinbox = QtWidgets.QSpinBox(self.NonlinearWidgetContents)
        self.non_max_iteration_spinbox.setGeometry(QtCore.QRect(207, 190, 45, 20))
        self.non_max_iteration_spinbox.setObjectName("max_iteration_spinbox")

        self.non_relative_error_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.non_relative_error_label.setGeometry(QtCore.QRect(262, 190, 120, 20))
        self.non_relative_error_label.setObjectName("relative_error_label")

        self.non_relative_error_spinbox = QtWidgets.QSpinBox(self.NonlinearWidgetContents)
        self.non_relative_error_spinbox.setGeometry(QtCore.QRect(380, 190, 45, 20))
        self.non_relative_error_spinbox.setObjectName("relative_error_spinbox")

        self.non_pushButton = QtWidgets.QPushButton(self.NonlinearWidgetContents)
        self.non_pushButton.setGeometry(QtCore.QRect(20, 230, 411, 28))
        self.non_pushButton.setObjectName("pushButton")
        self.non_pushButton.pressed.connect(self.solve_non_linear)

        self.non_result_label = QtWidgets.QLabel(self.NonlinearWidgetContents)
        self.non_result_label.setEnabled(True)
        self.non_result_label.setSizePolicy(sizePolicy)
        self.non_result_label.setObjectName("non_result_label")
        self.non_result_label.setMargin(5)

        self.non_scroll_area = QtWidgets.QScrollArea(self.NonlinearWidgetContents)
        self.non_scroll_area.setGeometry(QtCore.QRect(20, 276, 411, 0))
        self.non_scroll_area.setFixedWidth(411)
        self.non_scroll_area.setMaximumHeight(195)
        self.non_scroll_area.setWidget(self.non_result_label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.actionLinear.triggered.connect(self.linearWindowSize)
        self.actionNonlinear.triggered.connect(self.nonLinearWindowSize)

        self.main_combobox.currentIndexChanged['QString'].connect(self.linearChanges)
        self.non_main_combobox.currentIndexChanged['QString'].connect(self.nonLinearChanges)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def linearWindowSize(self):
        self.LinearscrollArea.show()
        self.NonlinearscrollArea.hide()
        MainWindow.setFixedHeight(540)
        MainWindow.resize(MainWindow.width(), 540)

    def nonLinearWindowSize(self):
        self.LinearscrollArea.hide()
        self.NonlinearscrollArea.show()
        MainWindow.setFixedHeight(314)
        MainWindow.resize(MainWindow.width(), 314)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical Solver"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionLinear.setText(_translate("MainWindow", "Linear"))
        self.actionNonlinear.setText(_translate("MainWindow", "Non-linear"))

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
        self.relative_error_label.setText(_translate("MainWindow", "Relative error (10^-"))
        self.decomposition_label.setText(_translate("MainWindow", "Decomposition form:"))

        self.precision_spinbox.setMaximum(10)
        self.precision_spinbox.setMinimum(3)

        self.max_iteration_spinbox.setMaximum(99)
        self.max_iteration_spinbox.setMinimum(2)

        self.relative_error_spinbox.setMaximum(8)
        self.relative_error_spinbox.setMinimum(1)

        self.precision_spinbox.setValue(self.default_precision)
        self.max_iteration_spinbox.setValue(self.default_iterations)
        self.relative_error_spinbox.setValue(self.default_epsilon)

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

        self.non_info_label.setText(_translate("MainWindow", "Enter function like\n"
                                                             "3x^2-4x+67\n"
                                                             "7x^3-12x^2+67"))
        self.non_info_label.setAlignment(QtCore.Qt.AlignCenter)

        self.fx_label.setText(_translate("MainWindow", "f(x):"))
        self.gx_label.setText(_translate("MainWindow", "g(x):"))
        self.fdashx_label.setText(_translate("MainWindow", "f'(x):"))

        self.xl_label.setText(_translate("MainWindow", "xl:"))
        self.xu_label.setText(_translate("MainWindow", "xu:"))
        self.xo_label.setText(_translate("MainWindow", "xo:"))

        self.non_precision_label.setText(_translate("MainWindow", "Precision:"))
        self.non_max_iteration_label.setText(_translate("MainWindow", "Iterations No:"))
        self.non_relative_error_label.setText(_translate("MainWindow", "Relative error (10^-"))

        self.non_precision_spinbox.setMaximum(10)
        self.non_precision_spinbox.setMinimum(3)

        self.non_max_iteration_spinbox.setMaximum(99)
        self.non_max_iteration_spinbox.setMinimum(2)

        self.non_relative_error_spinbox.setMaximum(8)
        self.non_relative_error_spinbox.setMinimum(1)

        self.non_precision_spinbox.setValue(self.default_precision)
        self.non_max_iteration_spinbox.setValue(self.default_iterations)
        self.non_relative_error_spinbox.setValue(self.default_epsilon)

        self.non_main_combobox.setItemText(0, _translate("MainWindow", "Bisection"))
        self.non_main_combobox.setItemText(1, _translate("MainWindow", "False-Position"))
        self.non_main_combobox.setItemText(2, _translate("MainWindow", "Fixed point"))
        self.non_main_combobox.setItemText(3, _translate("MainWindow", "Newton-Raphson"))
        self.non_main_combobox.setItemText(4, _translate("MainWindow", "Secant method"))

        self.non_pushButton.setText(_translate("MainWindow", "Solve"))

        self.xo_label.hide()
        self.xo_textbox.hide()

        self.gx_label.hide()
        self.gx_textbox.hide()

        self.fdashx_label.hide()
        self.fdashx_textbox.hide()

        self.NonlinearscrollArea.hide()

        MainWindow.setFixedHeight(self.scroll_area.height() + self.scroll_area.y() + 40)
        MainWindow.resize(MainWindow.width(), self.scroll_area.height() + self.scroll_area.y() + 40)

    def linearChanges(self):
        self.precision_spinbox.setValue(self.default_precision)
        self.max_iteration_spinbox.setValue(self.default_iterations)
        self.relative_error_spinbox.setValue(self.default_epsilon)

        if self.main_combobox.currentIndex() == 0 or self.main_combobox.currentIndex() == 1:
            self.none_pivoting.setChecked(True)
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
            self.partial_pivoting.setChecked(True)

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
            self.none_pivoting.setChecked(True)
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

    def nonLinearChanges(self):
        self.non_precision_spinbox.setValue(self.default_precision)
        self.non_max_iteration_spinbox.setValue(self.default_iterations)
        self.non_relative_error_spinbox.setValue(self.default_epsilon)

        if self.non_main_combobox.currentIndex() == 0 or self.non_main_combobox.currentIndex() == 1 or self.non_main_combobox.currentIndex() == 4:
            self.fx_label.show()
            self.fx_textbox.show()

            self.xl_label.show()
            self.xl_textbox.show()

            self.xu_label.show()
            self.xu_textbox.show()

            self.xo_label.hide()
            self.xo_textbox.hide()

            self.gx_label.hide()
            self.gx_textbox.hide()

            self.fdashx_label.hide()
            self.fdashx_textbox.hide()
        elif self.non_main_combobox.currentIndex() == 3:
            self.fx_label.show()
            self.fx_textbox.show()

            self.xl_label.hide()
            self.xl_textbox.hide()

            self.xu_label.hide()
            self.xu_textbox.hide()

            self.xo_label.show()
            self.xo_textbox.show()

            self.gx_label.hide()
            self.gx_textbox.hide()

            self.fdashx_label.show()
            self.fdashx_textbox.show()
        else:
            self.fx_label.hide()
            self.fx_textbox.hide()

            self.xl_label.hide()
            self.xl_textbox.hide()

            self.xu_label.hide()
            self.xu_textbox.hide()

            self.xo_label.show()
            self.xo_textbox.show()

            self.gx_label.show()
            self.gx_textbox.show()

            self.fdashx_label.hide()
            self.fdashx_textbox.hide()

    def solve_linear(self):
        self.iterations = self.max_iteration_spinbox.value()
        self.epsilon = self.relative_error_spinbox.value()

        coff = self.input_textbox.toPlainText().split('\n')
        if coff[0].find(',') == -1:
            coff[0] += ','
            return
        n = 0
        a = []
        b = []
        initial = []
        row_size = 0
        for i in range(len(coff)):
            try:
                eva = list(ast.literal_eval(coff[i]))
                a.append(eva[0:len(eva) - 1])
                b.append(eva[len(eva) - 1])
            except:
                coff_split = coff[i].split(',')
                eva = list()
                for num in coff_split:
                    try:
                        eva.append(float(num) if float(num) != int(num) else int(num))
                    except:
                        eva.append(0)
                a.append(list(eva[0:len(eva) - 1]))
                b.append(eva[len(eva) - 1])
            n += 1
            if n == 1:
                row_size = len(a[0])
            if row_size != len(a[n - 1]):
                self.result_label.setText(
                    f"Row(1) contains {row_size + 1} elements and row({n}) contains {len(a[n - 1]) + 1}"
                    " elements, So your input is invalid")
                self.result_label.adjustSize()
                self.scroll_area.resize(self.result_label.width(), self.result_label.height() + 25)
                MainWindow.setFixedHeight(self.scroll_area.height() + self.scroll_area.y() + 26)
                MainWindow.resize(MainWindow.width(), self.scroll_area.height() + self.scroll_area.y() + 26)
                return

        if n < row_size:
            self.result_label.setText(
                f"The number of rows({n}) should be one less than the number of columns({row_size + 1})")
            return
        elif n > row_size:
            self.result_label.setText(f"Matrix size must be {row_size + 1}x{row_size + 2}")
            return

        start = time.perf_counter()

        if self.main_combobox.currentText() == "jacobi" or self.main_combobox.currentText() == "gauss-seidel":
            try:
                row_size = len(list(ast.literal_eval(self.initial_guess_textbox.text())))
            except:
                row_size = 0
            if row_size == n:
                initial = list(ast.literal_eval(self.initial_guess_textbox.text()))
            else:
                initial = [0.0 for _ in range(n)]

        service = Service(self.precision_spinbox.value(), self.none_pivoting.isChecked(), self.partial_pivoting.isChecked()
                                                                                                    , self.complete_pivoting.isChecked())
        if self.main_combobox.currentText() == "LU-decomposition":
            massage = GaussFactory(self.decomposition_combobox.currentText(), service, n, a, b, initial, self.epsilon,
                                     self.iterations).create().execute()
        else:
            message = GaussFactory(self.main_combobox.currentText(), service, n, a, b, initial, self.epsilon,
                                     self.iterations).create().execute()

        self.result_label.setText(message + "\nTime taken: " + str(time.perf_counter() - start))
        self.result_label.adjustSize()
        self.scroll_area.resize(self.result_label.width(), self.result_label.height() + 5)
        MainWindow.setFixedHeight(self.scroll_area.height() + self.scroll_area.y() + 52)
        MainWindow.resize(MainWindow.width(), self.scroll_area.height() + self.scroll_area.y() + 52)

    def solve_non_linear(self):
        self.iterations = self.non_max_iteration_spinbox.value()
        self.epsilon = self.non_relative_error_spinbox.value()

        function = self.fx_textbox.toPlainText()
        derivative = self.fdashx_textbox.toPlainText()
        xl = self.xl_textbox.toPlainText() if  self.xl_textbox.toPlainText() else "0"
        xu = self.xu_textbox.toPlainText() if  self.xu_textbox.toPlainText() else "0"
        x_initial = self.xo_textbox.toPlainText() if  self.xo_textbox.toPlainText() else "0"

        if self.non_main_combobox.currentText() == "Fixed point" :
            function = self.gx_textbox.toPlainText()

        if not function:
            return

        if self.non_main_combobox.currentText() == "Newton-Raphson" and not derivative:
            x = Symbol('x')
            derivative = str(Derivative(eval(function), x).doit())

        service = Service(self.non_precision_spinbox.value())
        message = RootsFactory(self.non_main_combobox.currentText(), service, function, self.epsilon, self.iterations, xu, xl, x_initial, derivative).create().execute()
        print(message)

        self.non_scroll_area.resize(self.non_result_label.width(), self.non_result_label.height() + 5)
        MainWindow.setFixedHeight(self.non_scroll_area.height() + self.non_scroll_area.y() + 52)
        MainWindow.resize(MainWindow.width(), self.non_scroll_area.height() + self.non_scroll_area.y() + 52)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
