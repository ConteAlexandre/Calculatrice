# Import package for ui
from PySide2 import QtWidgets, QtGui

CUSTOM_FONT = QtGui.QFont()
CUSTOM_FONT.setPointSize(14)

# Initialize class
class ButtonCustom(QtWidgets.QPushButton):
    def __init__(self, texte):
        super().__init__(texte)
        # Here, we change the color button when we fly over
        self.setStyleSheet("QPushButton:hover {color: rgb(100, 200, 130);}")
        # Custom font of numbers
        self.setFont(CUSTOM_FONT)

    # Method for test when we get to the button
    def enterEvent(self, e):
        print("Bonjour")

    # Method for test when we leave to the button
    def leaveEvent(self, e):
        print("Bonsoir")