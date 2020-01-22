# Import package for ui
from PySide2 import QtWidgets, QtCore, QtGui
# Import packages for add argument with method
from functools import partial
# Import file created with QTDesigner and select specifically the name of the class
from Custom.ma_calculatrice import Ui_Form_calculatrice

# Initialization class for display window, and attribute the class of the file
class Calculatrie(Ui_Form_calculatrice, QtWidgets.QWidget):
    # Initialize method default for start
    def __init__(self):
        super().__init__()
        # Define the title of window
        # self.setWindowTitle("Calculatrice")
        # Here, we use the widgets we created in the file ma_calculatrice.py
        self.setupUi(self)
        # Method for use the loop specifically at setupUi
        self.modificationsetupUI()
        self.keyShortCut()
        # Define method for widgets
        # self.setup_ui()
        self.setup_connection()

    def modificationsetupUI(self):
        self.btn_all = []
        # Here, it's a loop for add parameter all PushButton by counting them
        for i in range(self.gridLayout.count()):
            # Recover an item with value of the loop, we specify that we wish to recover that widgets
            item = self.gridLayout.itemAt(i).widget()
            # If the widget is a instance of QPushButton and is only numeric
            if isinstance(item, QtWidgets.QPushButton) and item.text().isdigit():
                self.btn_all.append(item)

    # Method for define the shortcut in the application
    def keyShortCut(self):
        # loop for target specifically the pave numeric
        for btn in range(10):
            QtWidgets.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.numberPressed, str(btn)))

        QtWidgets.QShortcut(QtGui.QKeySequence('+'), self, partial(self.operationPressed, str(self.btn_addit.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('-'), self, partial(self.operationPressed, str(self.btn_soust.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('/'), self, partial(self.operationPressed, str(self.btn_div.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('*'), self, partial(self.operationPressed, str(self.btn_multi.text())))
        QtWidgets.QShortcut(QtGui.QKeySequence('Enter'), self, self.resultOperation)
        QtWidgets.QShortcut(QtGui.QKeySequence('Del'), self, self.delete)
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)

    # Method for initialize widgets without the file
    def setup_ui(self):
        # This widget is layout with widget
        self.layoutgrid = QtWidgets.QGridLayout(self)

        # Initialize all widgets edit
        self.ln_editOperation = QtWidgets.QLineEdit()
        self.ln_result = QtWidgets.QLineEdit("0")
        # Widgets for PushButton number
        self.btn_button0 = QtWidgets.QPushButton("0")
        self.btn_button1 = QtWidgets.QPushButton("1")
        self.btn_button2 = QtWidgets.QPushButton("2")
        self.btn_button3 = QtWidgets.QPushButton("3")
        self.btn_button4 = QtWidgets.QPushButton("4")
        self.btn_button5 = QtWidgets.QPushButton("5")
        self.btn_button6 = QtWidgets.QPushButton("6")
        self.btn_button7 = QtWidgets.QPushButton("7")
        self.btn_button8 = QtWidgets.QPushButton("8")
        self.btn_button9 = QtWidgets.QPushButton("9")
        # Widgets for PushButton operations
        self.btn_point = QtWidgets.QPushButton(".")
        self.btn_multi = QtWidgets.QPushButton("x")
        self.btn_div = QtWidgets.QPushButton("/")
        self.btn_addit = QtWidgets.QPushButton("+")
        self.btn_soust = QtWidgets.QPushButton("-")
        self.btn_egal = QtWidgets.QPushButton("=")
        self.btn_delete = QtWidgets.QPushButton("c")
        self.btn_pourcentage = QtWidgets.QPushButton("%")
        # Add widgets in the layout grid and placement position
        self.layoutgrid.addWidget(self.ln_editOperation, 0, 0, 1, 4)
        self.layoutgrid.addWidget(self.ln_result, 1, 0, 1, 4)
        self.layoutgrid.addWidget(self.btn_multi, 2, 3, 1, 1)
        self.layoutgrid.addWidget(self.btn_delete, 2, 0, 1, 1)
        self.layoutgrid.addWidget(self.btn_button1, 3, 0, 1, 1)
        self.layoutgrid.addWidget(self.btn_button2, 3, 1, 1, 1)
        self.layoutgrid.addWidget(self.btn_button3, 3, 2, 1, 1)
        self.layoutgrid.addWidget(self.btn_addit, 3, 3, 1, 1)
        self.layoutgrid.addWidget(self.btn_button4, 4, 0, 1, 1)
        self.layoutgrid.addWidget(self.btn_button5, 4, 1, 1, 1)
        self.layoutgrid.addWidget(self.btn_button6, 4, 2, 1, 1)
        self.layoutgrid.addWidget(self.btn_soust, 4, 3, 1, 1)
        self.layoutgrid.addWidget(self.btn_button7, 5, 0, 1, 1)
        self.layoutgrid.addWidget(self.btn_button8, 5, 1, 1, 1)
        self.layoutgrid.addWidget(self.btn_button9, 5, 2, 1, 1)
        self.layoutgrid.addWidget(self.btn_div, 5, 3, 1, 1)
        self.layoutgrid.addWidget(self.btn_button0, 6, 1, 1, 1)
        self.layoutgrid.addWidget(self.btn_pourcentage, 6, 0, 1, 1)
        self.layoutgrid.addWidget(self.btn_point, 6, 2, 1, 1)
        self.layoutgrid.addWidget(self.btn_egal, 6, 3, 1, 1)

        self.btn_all = []

        # Here, it's a loop for add parameter all PushButton by counting them
        for i in range(self.layoutgrid.count()):
            # Recover an item with value of the loop, we specify that we wish to recover that widgets
            item = self.layoutgrid.itemAt(i).widget()
            # If the widget is a instance of QPushButton
            if isinstance(item, QtWidgets.QPushButton):
                # About we define an other size
                item.setFixedSize(64, 64)
                if item.text().isdigit():
                    self.btn_all.append(item)

    # Initialize connection for widget
    def setup_connection(self):
        # loop because for each button, we wish add the text for different value
        for button in self.btn_all:
            # Class partial of module functools because permit add argument with method
            button.clicked.connect(partial(self.numberPressed, str(button.text())))

        # Connection for each button operation
        self.btn_div.clicked.connect(partial(self.operationPressed, str(self.btn_div.text())))
        self.btn_addit.clicked.connect(partial(self.operationPressed, str(self.btn_addit.text())))
        self.btn_soust.clicked.connect(partial(self.operationPressed, str(self.btn_soust.text())))
        self.btn_multi.clicked.connect(partial(self.operationPressed, str(self.btn_multi.text())))

        # Connection different for result and clear
        self.btn_egal.clicked.connect(self.resultOperation)
        self.btn_delete.clicked.connect(self.delete)

    # Method for button number when click
    def numberPressed(self, button):
        # Define variable to make it easier
        resultat = self.ln_result.text()
        # Condition for add in lineEdit result
        if resultat == "0":
            # Add the new number if value is 0
            self.ln_result.setText(button)
        # Else append the new number with the previous number
        else:
            self.ln_result.setText(resultat + button)

    # Method for widgets PushButton operation
    def operationPressed(self, operation):
        # Variable for recover text widget line edit Operation
        operationText = self.ln_editOperation.text()
        # Variable for recover text widget line edit Result
        result = self.ln_result.text()

        # Add the variables operationText, result and argument operation at widget lineEdit Operation
        self.ln_editOperation.setText(operationText + result + operation)
        # Then reinitialize the widget lineEdit Result
        self.ln_result.setText("0")

    # Method for calculate the operation in the widget
    def resultOperation(self):
        # Variable for to make to easier
        result = str(self.ln_result.text())
        # Add the new text in the widget for then calculate
        self.ln_editOperation.setText(self.ln_editOperation.text() + result)
        # Method eval permit to detect the symbol in the operation and calculate the result depending
        resultatOperation = eval(str(self.ln_editOperation.text()))
        # Replaces the lineEdit Result with this variable
        self.ln_result.setText(str(resultatOperation))

    # Method for reinitialize all widgets LineEdit
    def delete(self):
        self.ln_result.setText("0")
        self.ln_editOperation.clear()




# Initialize application
app = QtWidgets.QApplication()
# Initialize window
win = Calculatrie()
# Display windows
win.show()
# Start application
app.exec_()