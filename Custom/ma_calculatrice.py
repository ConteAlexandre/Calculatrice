# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatrice.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

# Here we import the customize on the PushButton, change directly in the application QTDesigner is better but some
# function will have to be write in the file
from Custom.buttoncustom import ButtonCustom

class Ui_Form_calculatrice(object):
    def setupUi(self, Form_calculatrice):
        if Form_calculatrice.objectName():
            Form_calculatrice.setObjectName(u"Form_calculatrice")
        Form_calculatrice.resize(256, 388)
        self.gridLayout = QGridLayout(Form_calculatrice)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_point = ButtonCustom(Form_calculatrice)
        self.btn_point.setObjectName(u"btn_point")
        self.btn_point.setMinimumSize(QSize(64, 64))
        self.btn_point.setMaximumSize(QSize(64, 64))
        self.btn_point.setFlat(True)

        self.gridLayout.addWidget(self.btn_point, 7, 2, 1, 1)

        self.btn_button3 = ButtonCustom(Form_calculatrice)
        self.btn_button3.setObjectName(u"btn_button3")
        self.btn_button3.setMinimumSize(QSize(64, 64))
        self.btn_button3.setMaximumSize(QSize(64, 64))
        self.btn_button3.setFlat(True)

        self.gridLayout.addWidget(self.btn_button3, 4, 2, 1, 1)

        self.btn_delete = ButtonCustom(Form_calculatrice)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(64, 64))
        self.btn_delete.setMaximumSize(QSize(64, 64))
        self.btn_delete.setFlat(True)

        self.gridLayout.addWidget(self.btn_delete, 3, 0, 1, 1)

        self.btn_pourcentage = ButtonCustom(Form_calculatrice)
        self.btn_pourcentage.setObjectName(u"btn_pourcentage")
        self.btn_pourcentage.setMinimumSize(QSize(64, 64))
        self.btn_pourcentage.setMaximumSize(QSize(64, 64))
        self.btn_pourcentage.setFlat(True)

        self.gridLayout.addWidget(self.btn_pourcentage, 7, 0, 1, 1)

        self.btn_button5 = ButtonCustom(Form_calculatrice)
        self.btn_button5.setObjectName(u"btn_button5")
        self.btn_button5.setMinimumSize(QSize(64, 64))
        self.btn_button5.setMaximumSize(QSize(64, 64))
        self.btn_button5.setFlat(True)

        self.gridLayout.addWidget(self.btn_button5, 5, 1, 1, 1)

        self.btn_div = ButtonCustom(Form_calculatrice)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setMinimumSize(QSize(64, 64))
        self.btn_div.setMaximumSize(QSize(64, 64))
        self.btn_div.setFlat(True)

        self.gridLayout.addWidget(self.btn_div, 6, 3, 1, 1)

        self.ln_result = QLineEdit(Form_calculatrice)
        self.ln_result.setObjectName(u"ln_result")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75);
        font.setKerning(True)
        self.ln_result.setFont(font)
        self.ln_result.setFrame(False)
        self.ln_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ln_result, 2, 0, 1, 4)

        self.btn_button2 = ButtonCustom(Form_calculatrice)
        self.btn_button2.setObjectName(u"btn_button2")
        self.btn_button2.setMinimumSize(QSize(64, 64))
        self.btn_button2.setMaximumSize(QSize(64, 64))
        self.btn_button2.setFlat(True)

        self.gridLayout.addWidget(self.btn_button2, 4, 1, 1, 1)

        self.btn_addit = ButtonCustom(Form_calculatrice)
        self.btn_addit.setObjectName(u"btn_addit")
        self.btn_addit.setMinimumSize(QSize(64, 64))
        self.btn_addit.setMaximumSize(QSize(64, 64))
        self.btn_addit.setFlat(True)

        self.gridLayout.addWidget(self.btn_addit, 4, 3, 1, 1)

        self.btn_button9 = ButtonCustom(Form_calculatrice)
        self.btn_button9.setObjectName(u"btn_button9")
        self.btn_button9.setMinimumSize(QSize(64, 64))
        self.btn_button9.setMaximumSize(QSize(64, 64))
        self.btn_button9.setFlat(True)

        self.gridLayout.addWidget(self.btn_button9, 6, 2, 1, 1)

        self.btn_egal = ButtonCustom(Form_calculatrice)
        self.btn_egal.setObjectName(u"btn_egal")
        self.btn_egal.setMinimumSize(QSize(64, 64))
        self.btn_egal.setMaximumSize(QSize(64, 64))
        self.btn_egal.setFlat(True)

        self.gridLayout.addWidget(self.btn_egal, 7, 3, 1, 1)

        self.btn_soust = ButtonCustom(Form_calculatrice)
        self.btn_soust.setObjectName(u"btn_soust")
        self.btn_soust.setMinimumSize(QSize(64, 64))
        self.btn_soust.setMaximumSize(QSize(64, 64))
        self.btn_soust.setFlat(True)

        self.gridLayout.addWidget(self.btn_soust, 5, 3, 1, 1)

        self.btn_button8 = ButtonCustom(Form_calculatrice)
        self.btn_button8.setObjectName(u"btn_button8")
        self.btn_button8.setMinimumSize(QSize(64, 64))
        self.btn_button8.setMaximumSize(QSize(64, 64))
        self.btn_button8.setFlat(True)

        self.gridLayout.addWidget(self.btn_button8, 6, 1, 1, 1)

        self.btn_button6 = ButtonCustom(Form_calculatrice)
        self.btn_button6.setObjectName(u"btn_button6")
        self.btn_button6.setMinimumSize(QSize(64, 64))
        self.btn_button6.setMaximumSize(QSize(64, 64))
        self.btn_button6.setFlat(True)

        self.gridLayout.addWidget(self.btn_button6, 5, 2, 1, 1)

        self.btn_button7 = ButtonCustom(Form_calculatrice)
        self.btn_button7.setObjectName(u"btn_button7")
        self.btn_button7.setMinimumSize(QSize(64, 64))
        self.btn_button7.setMaximumSize(QSize(64, 64))
        self.btn_button7.setFlat(True)

        self.gridLayout.addWidget(self.btn_button7, 6, 0, 1, 1)

        self.btn_multi = ButtonCustom(Form_calculatrice)
        self.btn_multi.setObjectName(u"btn_multi")
        self.btn_multi.setMinimumSize(QSize(64, 64))
        self.btn_multi.setMaximumSize(QSize(64, 64))
        self.btn_multi.setFlat(True)

        self.gridLayout.addWidget(self.btn_multi, 3, 3, 1, 1)

        self.btn_button1 = ButtonCustom(Form_calculatrice)
        self.btn_button1.setObjectName(u"btn_button1")
        self.btn_button1.setMinimumSize(QSize(64, 64))
        self.btn_button1.setMaximumSize(QSize(64, 64))
        self.btn_button1.setFlat(True)

        self.gridLayout.addWidget(self.btn_button1, 4, 0, 1, 1)

        self.btn_button4 = ButtonCustom(Form_calculatrice)
        self.btn_button4.setObjectName(u"btn_button4")
        self.btn_button4.setMinimumSize(QSize(64, 64))
        self.btn_button4.setMaximumSize(QSize(64, 64))
        self.btn_button4.setFlat(True)

        self.gridLayout.addWidget(self.btn_button4, 5, 0, 1, 1)

        self.btn_button0 = ButtonCustom(Form_calculatrice)
        self.btn_button0.setObjectName(u"btn_button0")
        self.btn_button0.setMinimumSize(QSize(64, 64))
        self.btn_button0.setMaximumSize(QSize(64, 64))
        self.btn_button0.setFlat(True)

        self.gridLayout.addWidget(self.btn_button0, 7, 1, 1, 1)

        self.ln_editOperation = QLineEdit(Form_calculatrice)
        self.ln_editOperation.setObjectName(u"ln_editOperation")
        self.ln_editOperation.setAutoFillBackground(False)
        self.ln_editOperation.setInputMask(u"")
        self.ln_editOperation.setFrame(False)
        self.ln_editOperation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ln_editOperation, 0, 0, 1, 4)


        self.retranslateUi(Form_calculatrice)

        QMetaObject.connectSlotsByName(Form_calculatrice)
    # setupUi

    def retranslateUi(self, Form_calculatrice):
        Form_calculatrice.setWindowTitle(QCoreApplication.translate("Form_calculatrice", u"Ma Calculatrice", None))
        self.btn_point.setText(QCoreApplication.translate("Form_calculatrice", u".", None))
        self.btn_button3.setText(QCoreApplication.translate("Form_calculatrice", u"3", None))
        self.btn_delete.setText(QCoreApplication.translate("Form_calculatrice", u"c", None))
        self.btn_pourcentage.setText(QCoreApplication.translate("Form_calculatrice", u"%", None))
        self.btn_button5.setText(QCoreApplication.translate("Form_calculatrice", u"5", None))
        self.btn_div.setText(QCoreApplication.translate("Form_calculatrice", u"/", None))
        self.ln_result.setText(QCoreApplication.translate("Form_calculatrice", u"0", None))
        self.btn_button2.setText(QCoreApplication.translate("Form_calculatrice", u"2", None))
        self.btn_addit.setText(QCoreApplication.translate("Form_calculatrice", u"+", None))
        self.btn_button9.setText(QCoreApplication.translate("Form_calculatrice", u"9", None))
        self.btn_egal.setText(QCoreApplication.translate("Form_calculatrice", u"=", None))
        self.btn_soust.setText(QCoreApplication.translate("Form_calculatrice", u"-", None))
        self.btn_button8.setText(QCoreApplication.translate("Form_calculatrice", u"8", None))
        self.btn_button6.setText(QCoreApplication.translate("Form_calculatrice", u"6", None))
        self.btn_button7.setText(QCoreApplication.translate("Form_calculatrice", u"7", None))
        self.btn_multi.setText(QCoreApplication.translate("Form_calculatrice", u"*", None))
        self.btn_button1.setText(QCoreApplication.translate("Form_calculatrice", u"1", None))
        self.btn_button4.setText(QCoreApplication.translate("Form_calculatrice", u"4", None))
        self.btn_button0.setText(QCoreApplication.translate("Form_calculatrice", u"0", None))
        self.ln_editOperation.setText("")
    # retranslateUi

